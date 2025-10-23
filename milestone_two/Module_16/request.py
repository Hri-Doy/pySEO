# Requesting an IP
import requests
url = 'https://api.ipify.org/?format=json'
response = requests.get(url)
data = response.json()
ip = data['ip']
print(f'Your IP address is {ip}.')

# Shortly: 
# response = requests.get(url).json()['ip']