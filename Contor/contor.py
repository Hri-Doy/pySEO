import httpx
import json
import base64
from pprint import pprint
from markdown import markdown

# Blog Writing System Prompt
with open('Contor/system_prompt.md', 'r', encoding="utf-8") as file:
    system_prompt = file.read()
# Blog Writing Actual Prompt
with open('Contor/blog_prompt.md', 'r', encoding="utf-8") as file:
    blog_prompt = file.read()

response = httpx.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer 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",
  },
  data=json.dumps({
    "model": "google/gemma-3-27b-it:free", # Optional
    "messages": [
      {
        "role": system_prompt,
        "content": blog_prompt
      }
    ]
  }),
  timeout=360.0
)

text_data = response.json().get('choices')
#pprint(text_data)
for data in text_data:
    msg = data.get('message').get('content')
    #pprint(msg)
# for text in text_data:
#     texts = text.get('message').get('content')

# WordPress Credentials and Configurations
username = 'pySeo_ws'
password = 'FPhI 4oB9 25C8 3HDC MXbS uOK0'
credentials = f'{username}:{password}'
token = base64.b64encode(credentials.encode())
wp_headers = {'Authorization':f'Basic {token.decode("utf-8")}'}

post_title = "ITIL Capability Maturity Model: Overview & Assessment"
wp_data = {
    'title' : post_title,
    'status' : 'publish',
    'content' : markdown(msg),
    'categories': 3
}

wp_endpoint = 'https://pyseo.ct.ws/wp-json/wp/v2/posts'
posted = httpx.post(wp_endpoint, json=wp_data, headers=wp_headers, timeout=360.0)
print(f"{post_title}____{posted.status_code}")