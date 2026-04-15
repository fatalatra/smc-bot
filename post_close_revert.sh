#!/bin/bash
# Revert POST_CLOSE_COOLDOWN: 300 → 1800 (one-shot, auto-rollback)
set -e
cp /root/smc-bot/config.py /root/smc-bot/config.py.bak_pcd_revert_$(date +%Y%m%d_%H%M%S)
sed -i 's|POST_CLOSE_COOLDOWN: int = 300   # 5 мин (temp 24h до ~2026-04-15 17:05 UTC)|POST_CLOSE_COOLDOWN: int = 1800  # 30 мин после ЛЮБОГО закрытия|' /root/smc-bot/config.py
systemctl restart smc-bot
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) reverted POST_CLOSE_COOLDOWN to 1800" >> /root/smc-bot/post_close_revert.log
