import requests
webhook_url = 'your webhook thingy'
while True:
    msg = {"content": "@everyone discord.gg/metadata"}
    response = requests.post(webhook_url, json=msg)
    if response.status_code == 204:
        print("posted")
    if response.status_code == 429:
        print("rate limited")

# code 429 is rate limited HTTPS request thing
# code 204 means that it posted the message
