import requests
webhook_url = 'https://discordapp.com/api/webhooks/1302025516668157972/HyRYt1WwX8TNIO0CICkVIJDy9vIxu0JIuK22scHWXmeVyDkohc__lnCg5gA8LNPD-1UO'
while True:
    a = {"content": "@everyone discord.gg/wxMmA57Wfv"}
    response = requests.post(webhook_url, json=a)
    if response.status_code == 204:
        print("posted")
    if response.status_code == 429:
        print("rate limited")

# code 429 is rate limited HTTPS request thing
# code 204 means that it posted the message
