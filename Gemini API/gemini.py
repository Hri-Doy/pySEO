import asyncio
import httpx
import base64
from google import genai

API_KEY = "AIzaSyAYK8IFI6F19v8HBBUiuG8CeC2qg5GfD80"

def ask_gemini(prompt):
    try:
        client = genai.Client(api_key=API_KEY)
        reply = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return reply.text
    except Exception as e:
        print(f"Error: {type(e).__name__}: {str(e)}")
        return None

async def main():
    # Creating the Content
    post_title = 'How to Make a Cup of tea'
    prompt = 'Write a simple article about making tea in one minute.'
    content = ask_gemini(prompt)
    
    if not content:
        print("Failed to generate content")
        return

    # wordpress credentials 
    username = 'pySEO'
    password = 'zb6g 1rKd Rswx c5Yb 01UU d3gS'
    credentials = f'{username}:{password}'
    token = base64.b64encode(credentials.encode())
    wp_headers = {'Authorization': f'Basic {token.decode("utf-8")}'}

    base_url = 'https://pyseo.ct.ws/wp-json/wp/v2'
    post_url = f'{base_url}/posts'

    data = {
        'title': post_title,
        'content': content,
        'status': 'publish'
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(post_url, headers=wp_headers, json=data)
    
    print("Response Code:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    asyncio.run(main())