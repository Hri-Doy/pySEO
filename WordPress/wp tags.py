import httpx
import base64
from pprint import pprint

base_url = 'https://restcountries.com/v3.1/region/europe'
r = httpx.get(base_url)
data = r.json()
#pprint(data)

capitals = []
for capital in data:
    capitally = capital.get('capital')
    for cap in capitally:
        capitals.append(cap)

username = 'SeoMind'
password = 'bzGY SXhO wsXg KS1u iU5j J4rq'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization': f'Basic {token.decode("utf-8")}'}


url_endpoint = 'https://seoz.wuaze.com/wp-json/wp/v2/tags'
for capital in capitals:
    data = {'name' : capital}
    r = httpx.post(url_endpoint, data=data, headers=wp_header)