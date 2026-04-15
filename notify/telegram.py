import os
import asyncio
import httpx
from dotenv import load_dotenv

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN", "")
TG_CHAT_ID = os.getenv("TG_CHAT_ID", "")
TG_BASE = f"https://api.telegram.org/bot{TG_TOKEN}"
TG_URL = f"{TG_BASE}/sendMessage"


async def send_tg(text: str):
    if not TG_TOKEN or not TG_CHAT_ID:
        print(f"[TG skip] {text}")
        return
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            await client.post(TG_URL, json={
                "chat_id": TG_CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
            })
    except Exception as e:
        print(f"[TG error] {e}")


async def tg_poll(handler):
    """Long-polls Telegram getUpdates and dispatches text messages from authorized chat to handler(text)."""
    if not TG_TOKEN or not TG_CHAT_ID:
        print("[TG poll] disabled — no token/chat_id")
        return
    offset = 0
    # On startup: drain backlog so we don't replay old commands after restart
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            r = await client.get(f"{TG_BASE}/getUpdates", params={"offset": -1, "timeout": 0})
            data = r.json()
            for upd in data.get("result", []):
                offset = max(offset, upd["update_id"] + 1)
        print(f"[TG poll] drained backlog, starting offset={offset}", flush=True)
    except Exception as e:
        print(f"[TG poll] init err: {e}", flush=True)

    while True:
        try:
            async with httpx.AsyncClient(timeout=40) as client:
                r = await client.get(
                    f"{TG_BASE}/getUpdates",
                    params={"offset": offset, "timeout": 30},
                )
                data = r.json()
                for upd in data.get("result", []):
                    offset = upd["update_id"] + 1
                    msg = upd.get("message") or upd.get("edited_message") or {}
                    chat_id = str(msg.get("chat", {}).get("id", ""))
                    if chat_id != TG_CHAT_ID:
                        continue
                    text = (msg.get("text") or "").strip()
                    if text:
                        try:
                            await handler(text)
                        except Exception as e:
                            print(f"[TG poll] handler err: {e}", flush=True)
        except Exception as e:
            print(f"[TG poll] err: {e}", flush=True)
            await asyncio.sleep(5)
