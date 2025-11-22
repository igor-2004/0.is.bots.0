import os
import sys

# Безопасный скрипт настройки, который запускается перед gunicorn.
# Он будет пытаться выполнить подготовительные действия ТОЛЬКО если задан BOT_TOKEN.
# Это предотвращает длинные Traceback в логах, если переменные окружения не настроены.

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("[server_setup] WARNING: BOT_TOKEN not set in environment. Skipping webhook setup and scheduler start.")
    print("[server_setup] Please set BOT_TOKEN (and other required env vars) in your Render/hosting settings and redeploy.")
    # Выходим с кодом 0, чтобы скрипт в background не падал с ошибкой и не засорял логи.
    # Основная проверка инициации бота происходит в самом gunicorn-процессе (server:app).
    sys.exit(0)

# Импортируем подготовительные функции только если токен есть
from server import prepare_webhook
from scheduler import start_scheduler

if __name__ == "__main__":
    try:
        prepare_webhook()
    except Exception as e:
        print("[server_setup] Error preparing webhook:", e)
    try:
        start_scheduler()
    except Exception as e:
        print("[server_setup] Error starting scheduler:", e)
    print("[server_setup] Server setup done.")
