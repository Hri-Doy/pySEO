import httpx
from pprint import pprint
city = 'Dhaka'
api = '26d3bea0e4249b3256bcce44d43cb73b'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

response = httpx.get(api_url).json()
country = response.get('sys').get('country')
print(f'Country Name: {country}')