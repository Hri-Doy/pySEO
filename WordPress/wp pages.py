import httpx
import base64
from pprint import pprint

# Gettting the data using API
base_url = 'https://restcountries.com/v3.1/all?fields=name'
req = httpx.get(base_url).json()

country_name = []
for i in req:
    names = i.get('name').get('common')
    country_name.append(names)
    
# Creating the wordpress pages

username = 'SeoMind'
password = 'bzGY SXhO wsXg KS1u iU5j J4rq'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization': f'Basic {token.decode("utf-8")}'}


endpoint_url = 'https://seoz.wuaze.com/wp-json/wp/v2/pages'
for page in country_name:
    data = {'page':country_name, 'status': 'draft', 'title': page}
    r = httpx.post(endpoint_url, data=data, headers=wp_header, timeout=60.0)
    print(r)
    
