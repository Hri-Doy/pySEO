from httpx import get

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
}

url = 'https://discovery-api.apollo.io/api/v1/discovery/modality/organizations/page_letters/a/pages'
res = get(url, headers=headers, timeout=360.0)
print(res.json())