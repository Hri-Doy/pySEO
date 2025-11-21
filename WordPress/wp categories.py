import httpx
import base64
from pprint import pprint
rest_countries = 'https://restcountries.com/v3.1/independent?status=true'

res = httpx.get(rest_countries)
api_data = res.json()
countries = []
for data in api_data:
    country_name = data.get('name').get('official')
    countries.append(country_name) # Storing the data in a list
    
wp_endpoints = 'https://seoz.wuaze.com/wp-json/wp/v2/categories'
username = 'SeoMind'
password = 'bzGY SXhO wsXg KS1u iU5j J4rq'
credentials = f'{username}:{password}'
token = base64.b64encode(credentials.encode())
wp_headeres = {'Authorization': f'Basic {token.decode("utf-8")}'}

for country in countries:
    data = {'name': country} # Preparing the Data
    r = httpx.post(wp_endpoints, data=data, headers=wp_headeres, timeout=60.0)
    print(r)