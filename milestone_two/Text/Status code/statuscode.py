from httpx import get

urls = [
    'https://www.google.com/',
    'https://pdcaconsulting.com/',
    'https://www.boonsoftware.com/',
    'https://prospectengine.com/'
]

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

for url in urls:
    r = get(url, headers=headers, timeout = 60.0)
    status_c = f'{url}---{r.status_code}'
    file = open('status codes.txt', 'a+')
    file.writelines(status_c + '\n')
    file.close()
    

# Reading the file:
file = open('status codes.txt', 'r+')
status_list = file.readlines()
file.close()

cleaned = [line.strip() for line in status_list]
for line in cleaned:
    print(line)

