import httpx
from pprint import pprint
access_token = 'f92fcd8284a0288ddb9211d6f1688925'
query = 'batman'
base_url = f'https://superheroapi.com/api/{access_token}/1'

r = httpx.get(base_url)
pprint(r)