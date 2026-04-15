"""Pause-state control for SMC bot — file-based flag, survives restarts."""
import os

PAUSE_FLAG = "/root/smc-bot/paused.flag"


def is_paused() -> bool:
    return os.path.exists(PAUSE_FLAG)


def set_paused(reason: str = "") -> None:
    with open(PAUSE_FLAG, "w") as f:
        f.write(reason)


def clear_paused() -> None:
    if os.path.exists(PAUSE_FLAG):
        os.remove(PAUSE_FLAG)


def pause_reason() -> str:
    if not os.path.exists(PAUSE_FLAG):
        return ""
    with open(PAUSE_FLAG) as f:
        return f.read().strip()
