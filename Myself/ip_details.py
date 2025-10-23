import requests
url = r'https://api.ipify.org/?format=json'
ip_request = requests.get(url).json().get('ip')
details_ip_url = f'http://ip-api.com/json/{ip_request}'
details_ip_request = requests.get(details_ip_url).json()
country = details_ip_request.get('country')
isp = details_ip_request.get('isp')
print(f'Your IP address is {ip_request} from {country} using {isp} isp.')