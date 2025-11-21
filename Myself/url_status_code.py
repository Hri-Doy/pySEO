import httpx

urls = [
    'https://www.google.com/',
    'https://www.gmail.com/',
    'https://www.dogfoodadviser.com/'
]

# one_url = 'https://www.google.com/'
# r = httpx.get(one_url).status_code
# print(r)

for url in urls:
    response = httpx.get(url).status_code
    print(url, response, sep="....")