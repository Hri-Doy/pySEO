from httpx import post
import base64

username = 'SeoMind'
password = 'bzGY SXhO wsXg KS1u iU5j J4rq'
credential = f'{username} : {password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization' : f'Basic {token.decode("utf-8")}'}

def wp_post(text):
    code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return code

title = 'The History of Bangladesh'
paragraph = 'The History of Bangladesh, a survey of the notable events and people in the history of Bangladesh, from the 3rd century bce to the present day. Bangladesh, located in the northeastern region of the Indian subcontinent, has been independently ruled since 1971, but the land and peoples of the modern country have centuries-long histories that centre on the thriving delta of the Ganges River. Dhaka is the capital of Bangladesh, having previously served as the capital city of Bengal province during the Mughal dynasty (1608–39 and 1660–1704), East Bengal province (1947), and East Pakistan (1956).'

wp_data = {
    'title' : title,
    'slug' : 'demo-post-slug',
    'content' : wp_post(paragraph),
    'categories' : 4,
    'status' : 'publish'
    
}

post_url = 'https://seoz.wuaze.com/wp-json/wp/v2/posts/'
r = post(post_url, data= wp_data, headers = wp_header)
print(r)