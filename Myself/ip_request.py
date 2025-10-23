import requests
url = r'https://api.ipify.org/?format=json'
request = requests.get(url)
data = request.json()['ip']
print(f'Your IP is {data}')