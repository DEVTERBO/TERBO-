from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/8bce6cc2fb0c63d65fab5.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/8bce6cc2fb0c63d65fab5.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/s_15_u")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/S_15_W")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6911536134").split()))


FAILED = "https://graph.org/file/8bce6cc2fb0c63d65fab5.jpg"
