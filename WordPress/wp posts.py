from httpx import post
from pprint import pprint
import base64

user = 'SeoMind'
password = 'SYg5 qshv tb7J WUSV N00U ETgo'
credential = f'{user}:{password}'
token = base64.b64encode(credential.encode())
headeres = {'Authorization' : f'Basic {token.decode("utf-8")}'}


data = {
    'title' : 'This is a post Title',
    'slug' : 'this/is/post/title',
    'content' : 'This is a content. Content, is this a content! Why do u think so? What makes u feel that way?',
    'status' : 'publish'
}


post_url = 'https://seoz.wuaze.com/wp-json/wp/v2/posts'
r = post(post_url, data=data, headers=headeres)
print(r)