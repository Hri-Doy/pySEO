from requests import get
from pprint import pprint

city_name = 'Dhaka'
API_key = '26d3bea0e4249b3256bcce44d43cb73b'
api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

r = get(api_url)

api_data = r.json()
country_name = api_data.get('sys').get('country')
weather_data = api_data.get('main')
feels_like = weather_data.get('feels_like')
temperature = weather_data.get('temp')
maximum_temp = weather_data.get('temp_max')
sea_level = weather_data.get('sea_level')

# print(country_name, temperature, feels_like, maximum_temp, sea_level, sep='\n')
print(f'Country: {country_name}', f'Temperature: {temperature}', f'Feels Like: {feels_like}', f'Maximum Temperature: {maximum_temp}', f'Sea Level: {sea_level}', sep='\n')