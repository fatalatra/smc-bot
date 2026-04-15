import hashlib
import hmac
import time
import json
import os
from typing import Optional
import httpx
from dotenv import load_dotenv
from exchange.models import Candle, Side, OrderType
from config import config

load_dotenv()

BROWSER_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json",
    "Origin": "https://futures.mexc.com",
    "Referer": "https://futures.mexc.com/",
}


class MexcFutures:
    BASE = "https://futures.mexc.com"

    def __init__(self):
        self.api_key = os.getenv("MEXC_API_KEY", "")
        self.api_secret = os.getenv("MEXC_API_SECRET", "")
        self.client = httpx.AsyncClient(
            timeout=httpx.Timeout(15.0, connect=8.0, read=15.0, write=10.0, pool=5.0),
            limits=httpx.Limits(max_keepalive_connections=0, max_connections=20),
            headers={**BROWSER_HEADERS, "Content-Type": "application/json"},
        )

    def _sign(self, timestamp: str, params: str = "") -> str:
        msg = self.api_key + timestamp + params
        return hmac.new(self.api_secret.encode(), msg.encode(), hashlib.sha256).hexdigest()

    def _auth_headers(self, params: str = "") -> dict:
        ts = str(int(time.time() * 1000))
        return {
            **BROWSER_HEADERS,
            "ApiKey": self.api_key,
            "Request-Time": ts,
            "Signature": self._sign(ts, params),
            "Content-Type": "application/json",
        }

    async def _public_get(self, path: str, params: dict = None) -> dict:
        r = await self.client.get(f"{self.BASE}{path}", params=params)
        return r.json()

    async def _private_get(self, path: str, params: dict = None) -> dict:
        param_str = ""
        if params:
            param_str = "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        r = await self.client.get(
            f"{self.BASE}{path}",
            params=params,
            headers=self._auth_headers(param_str),
        )
        return r.json()

    async def _private_post(self, path: str, data) -> dict:
        if isinstance(data, list):
            body = json.dumps(data)
        elif data:
            body = json.dumps(data)
        else:
            body = ""
        r = await self.client.post(
            f"{self.BASE}{path}",
            content=body,
            headers=self._auth_headers(body),
        )
        return r.json()

    # --- Public ---
    async def get_candles(self, symbol: str, interval: str, count: int = 200) -> list[Candle]:
        resp = await self._public_get(f"/api/v1/contract/kline/{symbol}", {"interval": interval, "limit": count})
        data = resp.get("data", {})
        if not data:
            return []
        candles = []
        times = data.get("time", [])
        opens = data.get("open", [])
        highs = data.get("high", [])
        lows = data.get("low", [])
        closes = data.get("close", [])
        vols = data.get("vol", [])
        for i in range(len(times)):
            candles.append(Candle(
                ts=times[i], open=opens[i], high=highs[i],
                low=lows[i], close=closes[i], volume=vols[i],
            ))
        return candles

    async def get_ticker(self, symbol: str) -> Optional[float]:
        resp = await self._public_get("/api/v1/contract/ticker", {"symbol": symbol})
        data = resp.get("data", {})
        return float(data.get("lastPrice", 0)) if data else None

    # --- Private ---
    async def get_balance(self) -> float:
        resp = await self._private_get("/api/v1/private/account/assets")
        for a in resp.get("data", []):
            if a.get("currency") == "USDT":
                return float(a.get("equity", 0))
        return 0.0

    async def get_available_balance(self) -> float:
        """Свободный баланс для открытия позиций"""
        resp = await self._private_get("/api/v1/private/account/assets")
        for a in resp.get("data", []):
            if a.get("currency") == "USDT":
                return float(a.get("availableBalance", 0))
        return 0.0

    async def set_leverage(self, symbol: str, leverage: int, pos_type: int = 1) -> dict:
        return await self._private_post("/api/v1/private/position/change_leverage", {
            "symbol": symbol,
            "leverage": leverage,
            "openType": 1,
            "positionType": pos_type,
        })

    async def get_positions(self, symbol: str) -> list:
        resp = await self._private_get("/api/v1/private/position/open_positions", {"symbol": symbol})
        return resp.get("data", []) or []

    async def place_order(self, symbol: str, side: Side, vol: int,
                          price: Optional[float] = None,
                          order_type: OrderType = OrderType.MARKET,
                          sl: Optional[float] = None,
                          tp: Optional[float] = None,
                          open_type: int = 1) -> dict:
        side_map = {Side.BUY: 1, Side.SELL: 3}
        data = {
            "symbol": symbol,
            "side": side_map[side],
            "type": 5 if order_type == OrderType.MARKET else 1,
            "vol": vol,
            "openType": open_type,
            "leverage": config.LEVERAGE,
        }
        if price and order_type == OrderType.LIMIT:
            data["price"] = price
        if sl:
            data["stopLossPrice"] = sl
        if tp:
            data["takeProfitPrice"] = tp
        return await self._private_post("/api/v1/private/order/submit", data)

    async def cancel_order(self, symbol: str, order_ids: list[str]) -> dict:
        return await self._private_post("/api/v1/private/order/cancel", order_ids)

    async def close_position(self, symbol: str, position: dict) -> dict:
        pos_type = position.get("positionType", 1)
        close_side = 2 if pos_type == 1 else 4
        data = {
            "symbol": symbol,
            "side": close_side,
            "type": 5,
            "vol": position.get("holdVol", 0),
            "openType": 1,
        }
        return await self._private_post("/api/v1/private/order/submit", data)

    async def close(self):
        await self.client.aclose()

    async def change_position_sl(self, symbol: str, position_id: str, sl_price: float) -> dict:
        """DEPRECATED — старый endpoint был неверный (change_margin). Не вызывать.
        Используй `get_stop_orders` + `change_stop_loss` для атомарного обновления SL.
        """
        raise NotImplementedError(
            "change_position_sl is deprecated — use get_stop_orders() + change_stop_loss(stop_plan_order_id, new_sl)"
        )

    async def get_stop_orders(self, symbol: str) -> list:
        """Активные SL/TP стоп-ордера по символу (только не-finished).
        Возвращает список объектов с ключами: id, positionId, stopLossPrice,
        takeProfitPrice, state, triggerSide, vol, version, и др.
        """
        r = await self._private_get(
            "/api/v1/private/stoporder/list/orders",
            {"symbol": symbol, "is_finished": 0, "page_num": 1, "page_size": 100},
        )
        return r.get("data", []) or []

    async def partial_close(self, symbol: str, pos_type: int, vol: int) -> dict:
        """Market close `vol` контрактов на открытой позиции.
        pos_type: 1=LONG (close via side=2), 2=SHORT (close via side=4).
        Не трогает остаток позиции.
        """
        close_side = 2 if pos_type == 1 else 4
        data = {
            "symbol": symbol,
            "side": close_side,
            "type": 5,  # market
            "vol": int(vol),
            "openType": 1,
        }
        result = await self._private_post("/api/v1/private/order/submit", data)
        print(f"[partial_close] symbol={symbol} pos_type={pos_type} vol={vol} resp={result}", flush=True)
        return result

    async def cancel_stop_order(self, stop_plan_order_id: int) -> dict:
        """Отмена stop-order (SL/TP plan-order) по id. Body — список объектов."""
        data = [{"stopPlanOrderId": int(stop_plan_order_id)}]
        result = await self._private_post("/api/v1/private/stoporder/cancel", data)
        print(f"[cancel_stop_order] id={stop_plan_order_id} resp={result}", flush=True)
        return result

    async def place_stop_order(self, position_id: int, vol: int,
                               stop_loss_price: float | None = None,
                               take_profit_price: float | None = None,
                               loss_trend: int = 1, profit_trend: int = 1) -> dict:
        """Создать новый SL/TP stop-order для существующей позиции.
        Endpoint: POST /api/v1/private/stoporder/place (rate 5/2s).
        lossTrend/profitTrend: 1=latest price trigger.
        """
        data = {
            "positionId": int(position_id),
            "vol": int(vol),
            "lossTrend": loss_trend,
            "profitTrend": profit_trend,
        }
        if stop_loss_price is not None:
            data["stopLossPrice"] = stop_loss_price
        if take_profit_price is not None:
            data["takeProfitPrice"] = take_profit_price
        result = await self._private_post("/api/v1/private/stoporder/place", data)
        print(f"[place_stop_order] pos={position_id} vol={vol} sl={stop_loss_price} tp={take_profit_price} resp={result}", flush=True)
        return result

    async def change_stop_loss(self, stop_plan_order_id: int, new_sl_price: float,
                               symbol: str = "BTC_USDT", loss_trend: int = 1) -> dict:
        """Атомарный update SL цены на существующем стоп-ордере.
        Endpoint: POST /api/v1/private/stoporder/change_plan_price (rate 4/2s).
        ВАЖНО: endpoint обнуляет поля которые не переданы, поэтому
        всегда читаем текущий TP и передаём его вместе с новым SL.
        """
        # Читаем текущий TP чтобы не потерять
        current_tp = None
        current_profit_trend = 1
        stops = await self.get_stop_orders(symbol)
        for s in stops:
            if s.get("id") == stop_plan_order_id:
                current_tp = s.get("takeProfitPrice")
                current_profit_trend = s.get("profitTrend", 1)
                break

        data = {
            "stopPlanOrderId": int(stop_plan_order_id),
            "stopLossPrice": new_sl_price,
            "lossTrend": loss_trend,
        }
        if current_tp:
            data["takeProfitPrice"] = current_tp
            data["profitTrend"] = current_profit_trend

        result = await self._private_post("/api/v1/private/stoporder/change_plan_price", data)
        print(f"[change_stop_loss] id={stop_plan_order_id} new_sl={new_sl_price} tp_preserved={current_tp} resp={result}", flush=True)
        return result

    async def get_history_orders(self, symbol: str, page_size: int = 100) -> list:
        """Fetch closed order history — contains profit, fee, positionId."""
        resp = await self._private_get(
            "/api/v1/private/order/list/history_orders",
            {"symbol": symbol, "page_size": page_size, "page_num": 1},
        )
        return resp.get("data", []) or []
