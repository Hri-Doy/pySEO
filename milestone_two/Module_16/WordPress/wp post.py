import httpx
import base64
wp_user = 'SeoMind'
wp_pass = 'IIsb IhQ1 lOeN fww0 Aa9T sgyx'
wp_credential = f'{wp_user}:{wp_pass}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}

data = {'title' : 'THis is an awesome Title'}
wp_post_url = 'https://seoz.wuaze.com/wp-json/wp/v2/posts'
res = httpx.post(wp_post_url, data=data, headers=wp_headers)
print(res.status_code)
print(res.json())