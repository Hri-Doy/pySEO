from httpx import get
from pprint import pprint

api = '52999339-bbb9ecedbdf4261e28b2e5861'
query = 'yellow+flowers'
base_url = f'https://pixabay.com/api/?key={api}&q={query}'

r = get(base_url).json()
data = r.get('hits')
for url in data:
    urls_list = url.get('largeImageURL')
    with open('flowers_urls.txt', 'a+') as file:
        file.writelines(urls_list + '\n')
    
with open('flowers_urls.txt', 'r+') as file:
    urls = file.readlines()
    new_urls = []
    for url in urls:
        clean_urls = url.strip('\n')
        new_urls.append(clean_urls)

i = 0
for url in new_urls:
    r = get(url)
    with open(f'image/{i}_pixi.jpg', 'wb') as file:
        file.write(r.content)
    i += 1