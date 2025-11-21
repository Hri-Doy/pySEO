from google import genai
from google.genai import types
import os
import base64
import httpx

api = 'AIzaSyDKaWJfiNIBikXRGeuis9Dh3UAvdlV0Wwc'
client = genai.Client(api_key=api)

system_prompt = 'You are a Semantic SEO entities friendly blog write with 20 years of instruction'
prompt = "Write a blog about, 'Top 10 rules of a Gentle Man'"

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
    'title' : 'Top 10 rules of a Gentle Man',
    'content' : response.text,
    'status' : 'publish',
}

url_endpoint = 'https://pyseo.ct.ws/wp-json/wp/v2/posts'
r = httpx.post(url_endpoint, data = wp_data, headers = wp_headeres, timeout=360.0)
print(r.status_code)