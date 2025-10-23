import requests

API = '26d3bea0e4249b3256bcce44d43cb73b'
city = input('Enter your city: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric'

response = requests.get(url).json().get('main')
temperature = response.get('temp')
temp_mininum = response.get('temp_min')
temp_miximum = response.get('temp_max')
feels_like = response.get('feels_like')

'''
City name: Dhaka
Temp :
Min :
Max :
Feels like:
'''

print(f'''
City Name: {city}
Temperature: {temperature}
Minimum Temp: {temp_mininum}
Maximum Temp: {temp_miximum}
Feels like: {feels_like}
''')

