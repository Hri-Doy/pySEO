from google import genai
from google.genai import types
import os
import base64
import httpx
from markdown import markdown

api = 'AIzaSyBbIH_UWKWm74Gbit-jM5NlGsI1AhUBNI4'
client = genai.Client(api_key=api)

system_prompt = """
You are an expert Semantic SEO blog writer with 20 years of experience.

Write in simple, easy English so anyone can understand clearly.
Focus on clarity, depth, topic authority, and smooth flow.

Use Markdown format only:
- Use clean headings (H2, H3) that flow logically.
- No unnecessary blank lines between sections.
- Maintain short, readable paragraphs.
- Never mention or list “entities” directly.

IMPORTANT FORMAT RULE:
You are STRICTLY FORBIDDEN from using horizontal lines or dividers of any kind.
This includes: "---", "___", "***", or any similar Markdown syntax.
If you need to separate sections, ONLY use headings (##, ###).
Never generate any horizontal rule under ANY condition.
This is a hard constraint.

Keep a conversational and friendly tone while staying professional.
"""

title = "Top 50 Rules of a Gentleman"
word_count = 1800

prompt = f"""
Write a full blog on the topic: {title}.
Target length: around {word_count} words.
Follow the system instructions strictly.
"""


response = client.models.generate_content(
    model = 'models/gemini-flash-latest',
    contents = prompt,
    config = types.GenerateContentConfig(
        system_instruction= system_prompt
    )
)
#print(response.text)

# This is a WordPress Credentials with Configuration
username = 'pySeo_ws'
password = 'FPhI 4oB9 25C8 3HDC MXbS uOK0'
credential = f'{username}:{password}'
token = base64.b64encode(credential.encode())
wp_headeres = {'Authorization' : f'Basic {token.decode("utf-8")}'}

wp_data = {
    'title' : title,
    'content' : markdown(response.text),
    'status' : 'publish',
}

url_endpoint = 'https://pyseo.ct.ws/wp-json/wp/v2/posts'
r = httpx.post(url_endpoint, data = wp_data, headers = wp_headeres, timeout=360.0)
print(r.status_code)