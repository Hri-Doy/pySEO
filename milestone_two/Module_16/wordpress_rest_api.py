from httpx import get
from pprint import pprint

base_url = 'https://tjarnir.fo/wp-json/wp/v2'
pages_api = f'{base_url}/pages' # Endpoint

r = get(pages_api)
api_data = r.json()

for page in api_data:
    print(page.get('link'))
