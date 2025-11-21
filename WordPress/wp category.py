import httpx
import base64

api_url = 'https://countrycode.org/api/countryCode/countryMenu'
categori_endpoints = 'https://dev-atire.pantheonsite.io/wp-json/wp/v2/categories'

def slugify(text):
    slug_text = text.strip().replace(' ', '-')
    return slug_text

def wp_category_create(url, data):
    username = 'Saddam'
    password = '7Cb3 MwcN ejk0 6IV5 lzww bQg6'
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    wp_header = {'Authorization': f'Basic: {token.decode("utf-8")}'}
    res = httpx.post(url, json=data, headers=wp_header)
    return res.status_code
    


respond = httpx.get(api_url)
if respond.status_code == 200:
    countires = respond.json()
    for country in countires:
        name = country.get('name')
        slug = slugify(name)
        data = {'name':name, 'slug':slug}
        wp_category_create(categori_endpoints, data)
        print(name, 'Category Created')