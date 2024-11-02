import requests
webhook_url = 'https://discordapp.com/api/webhooks/1302025516668157972/HyRYt1WwX8TNIO0CICkVIJDy9vIxu0JIuK22scHWXmeVyDkohc__lnCg5gA8LNPD-1UO'
message = {"content": "put ya message here and uh u can still do cool discord stuff like the cool fonts by doing **this**"}
print(f"Sending message to: {webhook_url}\nclick the link to see the webhook thingy\n\n\n\nignore all the random print below if it pops up.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
response = requests.post(webhook_url, json=message)
if response.status_code == 204:
    print('\nsent calm luh msg')
