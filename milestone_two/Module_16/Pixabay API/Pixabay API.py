from httpx import get 
from pprint import pprint
base_url = 'https://pixabay.com/api/'
pixabay_api = '52999339-bbb9ecedbdf4261e28b2e5861'
query = input('Searh for Free images..')

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

# https://pixabay.com/api/?key=52999339-bbb9ecedbdf4261e28b2e5861&q=yellow+flowers&image_type=photo&pretty=true
api_url = f'{base_url}?key={pixabay_api}&q={query}'
r = get(api_url, headers=headers, timeout=30.0).json().get('hits')
# pprint(r)
for urls in r:
    try:
        #print(urls.get('webformatURL'))
        image_urls = urls.get('webformatURL')
        file = open('image urls.txt', 'a+')
        file.writelines(image_urls + '\n')
        file.close()
    except:
        print('Not Found')
