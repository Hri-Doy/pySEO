from httpx import get
base_url = 'https://rawznaturalpetfood.com/wp-json/wp/v2'
page = 1
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
while True:
    api_url = f'{base_url}/posts?page={page}'
    response = get(api_url, headers=headers, timeout = 60.0)
    data = response.json()
    
    if not data or response.status_code != 200:
        break
    
    for posts in data:
        try:
            print(posts.get('link'))
        except:
            print('Posts not Found')
    
    page += 1