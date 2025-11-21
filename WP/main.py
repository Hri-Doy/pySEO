import httpx
import json
import base64

# WordPress Credentials 
username = 'SeoMind'
password = 'gF1q Y63u b85w wUIk dPzG e8FP'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization': f'Basic {token.decode("utf-8")}'}



server_url = 'https://mobile-phone-server.vercel.app/phones'
res = httpx.get(server_url)
if res.status_code == 200:
    data = res.json()
    phones = data.get("RECORDS")
    # print(phones[0])


# Wordpress Image Function

def media_from_url(img_src, img_name):
    """
    This will return the wordpress media from the URL.
    """
    codes = f'<!-- wp:image {{"sizeSlug":"large","align":"center"}} -->'\
            f'<figure class="wp-block-image aligncenter size-large">'\
            f'<img src="{img_src}"alt="{img_name}"/>'\
            f'<figcaption class="wp-element-caption">{img_name}</figcaption></figure>'\
            f'<!-- /wp:image -->'
    return codes

def dictionary_table(dictionary):
    '''
    This will generate wordpress gutenburg table from Dictionary
    :param dictionary:
    :return html table string
    '''
    code = f'<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        code += tr_data
    code += '</tbody></table></figure><!-- /wp:table -->'
    return code


def wp_paragraph(text):
    '''
    This will generate wordpress gutenburg paragraph
    '''
    paragraph = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return paragraph

def wp_heading_two(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'

# This is for content
def concatenate_string(*args):
    final =''
    for arg in args:
        final += arg
    return final

def slugify(name):
    code = name.strip().replace(' ','-')
    return code
    
def create_wp_post(title, content, slug, excerpt, status='publish'):
    api_url = 'https://seoz.wuaze.com/wp-json/wp/v2/posts'
    data = {
        'title': title,
        'content' : content,
        'slug': slug,
        'status': status,
        'excerpt':excerpt
    }
    response = httpx.post(api_url, json=data,headers=wp_header, timeout=360.0)
    print(f'{title} is posted')
    

for phone in phones:
    name = phone.get('name').title()
    released_at = phone.get('released_at').lower().replace('Released', '')
    chipset = phone.get('chipset')
    body = phone.get('body')
    os = phone.get('os')
    picture = phone.get('picture')
    
    first_dictionary = {
        'name' : name,
        'released_at' : released_at,
        'chipset' : chipset,
        'body' : body
    }
    
    first_paragraph = f'{name} has been {released_at}. It comes with {chipset} chipset. The body of this mobile is {body}. {os} is the built  in android version.'
    article_paragraph = wp_paragraph(first_paragraph)
    first_image = media_from_url(picture, name)
    first_heading = wp_heading_two(f'{name} Overview')
    first_table = dictionary_table(first_dictionary)
    
    # Specification Section (Converted from String to JSON)
    second_heading = wp_heading_two (f'{name} Specifications')
    specification_string = phone.get('specifications')
    specifications = json.loads(specification_string)
    second_table = dictionary_table(specifications)
    
    content = concatenate_string(
        article_paragraph,
        first_image,
        first_heading,
        first_table,
        second_heading,
        second_table)
    
    slug = slugify(name)
    excerpt = first_paragraph
    create_wp_post(name, content, slug, excerpt, status='publish')




