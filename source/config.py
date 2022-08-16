import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","BAAUb8nVPFi5xI-OxdwVJSJOGmmPfsxXGlqQ9iW4CWYzNyCPXi61R6OAF6uzRRJmx_NlQ0bVU3fMNbZxwfukzj8TcaZNjlgfilasoAh816KcDIAfGY2xYNdd4xvHwjbcUYx-2vzrqWRDDTL_fNzWYqx1uIcJpxqVQZStsYssT_k89iuG9d1reB59WYnMLj2nu7TRdbH8XSyVXK4oEjnfZsvbrqgRlv0yen9DhBLJ1LVC3oIVWCndApvZuoV-SaU7kdyhwHU4T9ZS_Wp5vsbSRVw-X4hsp8QH5Ntr792uq17KaSibNlRmr9lxhDVD4PCNQ29XLSiq-GyNm0O6ndgPi5gHeBg3QQA")
BOT_TOKEN = getenv("BOT_TOKEN","5511729718:AAEe3hUQUEk-aYPNvHxxnddiuoaYffu4uFo")
API_ID = int(getenv("API_ID","16416474"))
MONGODB_URL = getenv("MONGODB_URL")
API_HASH = getenv("API_HASH","88661a93ee10d24229b12a9127a88af6")
OWNER_NAME = getenv("OWNER_NAME", "G_G_6_6")
MONGODB_URL = getenv("MONGODB_URL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vlorantt")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4c7636b9c50116387d9f6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1914163949").split()))
