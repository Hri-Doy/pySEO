import requests
url = r'https://api.ipify.org/?format=json'
request = requests.get(url)
ip = request.json().get('ip')
ip_details = f'http://ip-api.com/json/{ip}'
response = requests.get(ip_details)
new_data = response.json()

'''
Your IP address is 123456 is located in Bangladesh. You are using ISP.
'''
country = new_data.get('country')
isp = new_data.get('isp')

#print(country, isp)
print(f'Your IP address is {ip} is located in {country}. You are using {isp} ISP.')