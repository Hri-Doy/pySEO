from httpx import get
from pprint import pprint
api = '52999339-bbb9ecedbdf4261e28b2e5861'
query = 'yellow+flowers'

api_url = f'https://pixabay.com/api/?key={api}&q={query}'
request = get(api_url).json()
data = request.get('hits')

# Large Images URLS
for urls in data:
    links = urls.get('largeImageURL')
    # print(links)

# Storing the images
    with open('images.txt', 'a+') as file:
        file.writelines(links + '\n')
    
# Reading the images
with open('images.txt', 'r+') as file:
    urls_list  = file.readlines()
    
# Removing the \n from the urls
new_urls_list = []
for urls in urls_list:
    new_url = urls.strip('\n')
    new_urls_list.append(new_url)

i = 0
for url in new_urls_list:
    r = get(url)
    with open(f'{i}_pixa.jpg', 'wb') as file:
        file.write(r.content)
    i += 1
    
# i = 0
# for url in new_urls_list:
#     r = get(url)
#     with open(f'{i}_pixa.jpg', 'wb') as file:
#         file.write(r.content)