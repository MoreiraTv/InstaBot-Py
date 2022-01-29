from __init__ import InstagramBot

with open("./credentials/token_value.txt", "r", encoding="utf-8") as tf:
    cookie_value = tf.read()

with open("./credentials/token_expiration.txt", "r", encoding="utf-8") as tf:
    cookie_expiration = tf.read()

jhonatanBot = InstagramBot(
    { "domain": ".instagram.com", "expirationDate": cookie_expiration, "httpOnly": True, "name": "sessionid", "path": "/", "secure": True, "session": False, "value": cookie_value},
) # Entre com o usuário e senha aqui

jhonatanBot.login()

