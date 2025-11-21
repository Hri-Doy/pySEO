from httpx import get
base_url = 'https://pdcaconsulting.com/wp-json/wp/v2'
page = 1 # Now while loop
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
while True:
    api_url = f'{base_url}/posts?page={page}'
    response =get(api_url, headers=headers, timeout=60.0)
    data = response.json()

    if not data or response.status_code != 200:
        break
    
    for posts in data:
        try:
            links = posts.get('link')
            file = open('pdcaposts.txt', 'a+')
            file.writelines(links + '\n')
            file.close()
        except:
            print('Not found links')
    page += 1
    
    
