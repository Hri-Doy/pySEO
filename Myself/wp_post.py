from httpx import get
from pprint import pprint

base_url = 'https://pdcaconsulting.com/wp-json/wp/v2'
api_url = f'{base_url}/posts?per_page=70'

r = get(api_url)
api_data = r.json()

for posts in api_data:
    try:
        print(posts.get('slug'))
    except:
        print('Page Not Found')