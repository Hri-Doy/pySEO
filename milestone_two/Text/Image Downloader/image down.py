from httpx import get
from pprint import pprint

api = '52999339-bbb9ecedbdf4261e28b2e5861'
base_url = 'https://pixabay.com/api'
query = input('Search for free images..')
api_url = f'{base_url}/?key={api}&q={query}'

r = get(api_url).json()
data = r.get('hits')

for urls in data:
    img_urls = urls.get('webformatURL') 
    # Storing the images
    with open('image urls.txt', 'a+') as file:
        file.writelines(img_urls + '\n') 
        
# Reading the stored images
with open('image urls.txt', 'r+') as file:
    urls_list = file.readlines()

# Removing the \n from the list
new_urls = []
for url in urls_list:
    new_url = url.rstrip('\n')
    new_urls.append(new_url)
    

print(new_urls)
    