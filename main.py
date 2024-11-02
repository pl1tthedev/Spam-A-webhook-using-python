import requests
webhook_url = 'https://discordapp.com/api/webhooks/1302025516668157972/HyRYt1WwX8TNIO0CICkVIJDy9vIxu0JIuK22scHWXmeVyDkohc__lnCg5gA8LNPD-1UO'
message = {"content": "spam1"}
response = requests.post(webhook_url, json=message)
messagee = {"content": "spam2"}
response = requests.post(webhook_url, json=messagee)
messageee = {"content": "spam3"}
response = requests.post(webhook_url, json=messageee)
messagea = {"content": "spam1"}
response = requests.post(webhook_url, json=messagea)
messageea = {"content": "spam2"}
response = requests.post(webhook_url, json=messageea)
messageeea = {"content": "spam3"}
response = requests.post(webhook_url, json=messageeea)
messageb = {"content": "spam1"}
response = requests.post(webhook_url, json=messageb)
messageeb = {"content": "spam2"}
response = requests.post(webhook_url, json=messageeb)
messageeeb = {"content": "spam3"}
response = requests.post(webhook_url, json=messageeeb)
if response.status_code == 204:
  print(f"Sending message to: {webhook_url}\nclick the link to see the webhook thingy\n\n\n\nignore all the random print below if it pops up.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
