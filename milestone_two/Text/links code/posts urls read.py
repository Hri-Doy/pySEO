from httpx import get 

base_url = 'https://prospectengine.com/wp-json/wp/v2'

# https://www.whatismybrowser.com/detect/what-is-my-user-agent/
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

page = 1
while True:
    api_url = f'{base_url}/posts?page={page}'
    request = get(api_url, headers=headers, timeout = 60.0)
    data = request.json()
    
    if not data or request.status_code != 200:
        break
    
    for posts in data:
        try:
            # print(posts.get('link'))
            # Save the posts in urls.txt file
            links = posts.get('link')
            file = open('urls.txt', 'a+')
            file.writelines(links + '\n')
            file.close()
        except:
            print('Nothing Found')
    page += 1
    
    
# Reading the urls.txt file links

file = open('urls.txt', 'r+')
urls_cleaned = file.readlines()
file.close()

cleaned = [line.strip() for line in urls_cleaned]
for line in cleaned:
    print(line)