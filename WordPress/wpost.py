from httpx import post
import base64

username = 'SeoMind'
password = 'SYg5 qshv tb7J WUSV N00U ETgo'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_headeres = {'Authorization' : f'Basic {token.decode("utf-8")}'}

def wp_para(text):
    return f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'

def wp_headingtwo(text):
    return f'<!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'

title = 'The History of Bangladesh'
intro = 'The history of Bangladesh, a survey of the notable events and people in the history of Bangladesh, from the 3rd century bce to the present day. Bangladesh, located in the northeastern region of the Indian subcontinent, has been independently ruled since 1971, but the land and peoples of the modern country have centuries-long histories that centre on the thriving delta of the Ganges River. Dhaka is the capital of Bangladesh, having previously served as the capital city of Bengal province during the Mughal dynasty (1608–39 and 1660–1704), East Bengal province (1947), and East Pakistan (1956).'
h2 = 'Buddhist, Hindu, and Muslim dynasties until about 1700'
body = 'From the 3rd century bce Buddhism flourished as the Mauryan emperors extended their influence in Bengal. Under the Gupta kings, who reigned from the early 4th to the late 6th century ce, Hinduism reestablished its hold, but Buddhism did not fully disappear. The two religions coexisted under the Pala dynasty (8th–12th century), as well as under the Chandra dynasty (10th–11th century) in the southeast. By the end of the 11th century, the Senas, who were strongly Hindu, had gained control over a large part of Bengal. As early as the 9th century, Arab traders brought Islam to Bengal. About 1200, Muslim invaders from the northwest overthrew the Senas. Muslim rule culminated in the Mughal dynasty (16th–18th century). In eastern Bengal, as in much of the northern part of the Indian subcontinent, Islam became the religion of the majority.'


wp_content = (
    wp_para(intro) + 
    wp_headingtwo(h2) +
    wp_para(body)
)

wp_data = {
    'title' : title,
    'content' : wp_content,
    'categories': 4,
    'status' : 'publish',
}

url_endpoint = 'https://seoz.wuaze.com/wp-json/wp/v2/posts'
r = post(url_endpoint, data = wp_data, headers = wp_headeres)
print(r)