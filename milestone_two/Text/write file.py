
# open, create, read/write.append , close
# text = 'This is a semple text'
# file = open('abc.txt', 'a+' )
# file.writelines(text +'\n')
# file.close()

from httpx import get

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}
urls = [
    'https://www.whatismybrowser.com/',
    'https://www.google.com/',
    'https://prospectengine.com/',
    'https://pdcaconsulting.com/',
    'https://www.boonsoftware.com/'
]

for url in urls:
    r = get(url, headers=headers, timeout=30.0)
    text = f'{url}---{r.status_code}'
    file = open('links.txt', 'a+')
    file.writelines(text + '\n')
    file.close()
