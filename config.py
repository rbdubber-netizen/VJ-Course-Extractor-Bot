# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

api_id = int(os.environ.get("API_ID", "33882007"))
api_hash = os.environ.get("API_HASH", "799677df02c75c218e83f74a70c1eef9")
bot_token = os.environ.get("BOT_TOKEN", "8819125289:AAGM8PRceRlJ-qc025kukzHuJl8OGhW9_cc")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "8137189417").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")

# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
