from httpx import get
from pprint import pprint
api = '52999339-bbb9ecedbdf4261e28b2e5861'
query = 'yellow+flowers'
api_endpoint = f'https://pixabay.com/api/?key={api}&q={query}'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
}
r = get(api_endpoint).json()
data = r.get('hits')
for url in data:
    links = url.get('largeImageURL')
    #Storing The Image
    with open('img_urls.txt', 'a+') as file:
        file.writelines(links + '\n')
 
 
with open('img_urls.txt', 'r+') as file:
    links = file.readlines()        
    
    new_links = []
    for url in links: 
        cln_links = url.strip('\n')
        new_links.append(cln_links)
        print(new_links)
    
i = 0
for urls in new_links:
    r = get(urls)
    with open(f'{i}_pic.jpg', 'wb') as file:
        file.write(r.content)
    i += 1