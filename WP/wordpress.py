import httpx
import base64
import json


'''
# Server Url data
# WP Image Function
# WP Dictionary to Table Function
# WP paragraph Function
# For Loop: for phone in phones (name, picture, released. body, os, storage)
# Generate an article
# Get the article data (name,released_at, chipset, body, os)
# Format the data like name title, remove released form release etc.
# Get the picture & Write the function : first_image 
# WP Heading two function
# First table (first_dictionary) & First Dictionary 
# specifications section
# convert specifiactions string to JSON
# Second heading
# second_table = wp_dictionary_table(specifications)
# Content format generation: def concatenate_string
# WordPress Authentication Connection
# WordPress post Function: def create_wp_post
# Wordpress post slug function slugify
'''

username = 'SeoMind'
password = 'gF1q Y63u b85w wUIk dPzG e8FP'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_header = {'Authorization':f'Basic {token.decode("utf-8")}'}



server_url = 'https://mobile-phone-server.vercel.app/phones'

respond = httpx.get(server_url)
if respond.status_code ==200:
    data = respond.json()
    phones = data.get('RECORDS')
    

def wp_image(image_src,image_name, image_alt):
    '''
    This function returns image for WordPress
    '''
    codes = f'<!-- wp:image {{"sizeSlug":"large","align":"center"}} -->'\
            f'<figure class="wp-block-image aligncenter size-large">'\
            f'<img src="{image_src}" alt="{image_alt}"/>'\
            f'<figcaption class="wp-element-caption">{image_name}</figcaption>'\
            f'</figure><!-- /wp:image -->'
    return codes

def wp_dictionary_table(dictionary):
    '''
    This function converts dictionary to table
    '''
    codes = f'<!-- wp:table --><figure class="wp-block-table"><table class="has-fixed-layout"><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes

def wp_paragraph(text):
    '''
    This function generates html paragraph for WordPress post.
    '''
    codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes

def wp_heading_two(text):
    codes = f'<!-- wp:heading --><h2 class="wp-block-heading">{text}</h2><!-- /wp:heading -->'
    return codes

def concatenate_string(*args):
    final =''
    for arg in args:
        final += arg
    return final

def slugify(name):
    codes = name.strip().replace(' ', '-')
    return codes

def create_wp_post(title, content, slug, excerpt, status='draft'):
    api_url = 'https://seoz.wuaze.com/wp-json/wp/v2/posts'
    data = {
        'title' : title,
        'content' : content,
        'slug' : slug,
        'status' : status,
        'excerpt' : excerpt
    }
    
    response = httpx.post(api_url, headers=wp_header, json=data)
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
    
    first_paragraph = f'{name} has been {released_at}. It comes with {chipset} chipset. The body of the mobile is {body}. {os} is the built in android version'
    article_paragraph = wp_paragraph(first_paragraph)
    first_image = wp_image(picture, name, f'{name} image')
    first_heading = wp_heading_two(f'{name} Overview')
    first_table = wp_dictionary_table(first_dictionary)
    
    # Specification Section
    second_heading = wp_heading_two(f'{name} Specifications')
    specifications_str = phone.get('specifications')
    specifications = json.loads(specifications_str)
    second_table = wp_dictionary_table(specifications)
    
    content = concatenate_string(
        article_paragraph,
        first_image,
        first_heading,
        first_table,
        second_heading,
        second_table)
    
    slug = slugify(name)
    excerpt = first_paragraph
    create_wp_post(name, content,slug, excerpt, status='draft')