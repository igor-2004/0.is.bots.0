import os

# Обязательные: задаются как переменные окружения на Render или в .env при локальной разработке
BOT_TOKEN = os.environ.get("8073733884:AAHRpXo9yZ3LTGeaYJD03fuzx1vRChlpa4k")  # ОБЯЗАТЕЛЬНО
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set in environment!")

# ID канала или чат-ид для публикации (например: -1001234567890)
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001958513038"))

# ID владельца/админа (Telegram user id)
OWNER_ID = int(os.environ.get("OWNER_ID", "1184497918"))

# Путь к sqlite (если используете Render disk — укажите /data/bot_database.db)
DB_PATH = os.environ.get("DB_PATH", "/data/bot_database.db")

# Вебхук: публичный URL (без пути)
# Пример: https://your-service.onrender.com
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")

# Путь приёма вебхуков (можно оставить /webhook)
WEBHOOK_PATH = os.environ.get("WEBHOOK_PATH", "/webhook")

# Ограничения/настройки
SEND_COOLDOWN_SECONDS = int(os.environ.get("SEND_COOLDOWN_SECONDS", 30 * 60))  # 30 минут по умолчанию
USE_OVERLAY_ON_IMAGE = os.environ.get("USE_OVERLAY_ON_IMAGE", "False").lower() in ("1","true","yes")

