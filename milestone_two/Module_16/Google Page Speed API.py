import requests

api = 'AIzaSyCwjqYkU8xsf08wNfPfJFPOtyDOoD4VpIg'
site = 'https://pdcaconsulting.com/'
#url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://pdcaconsulting.com/&key=AIzaSyCwjqYkU8xsf08wNfPfJFPOtyDOoD4VpIg"
url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={site}&key={api}'
response = requests.get(url).json()
fcp = response.get('lighthouseResult').get('audits').get('first-contentful-paint').get('score')
lcp = response.get('lighthouseResult').get('audits').get('largest-contentful-paint').get('score')
cls = response.get('lighthouseResult').get('audits').get('cumulative-layout-shift').get('score')

#print(f'Your site is: {site}, FCP: {fcp}, LCP: {lcp}, CLS: {cls}', sep='\n')
print(f'Your site is {site}', f'FCP : {fcp}', f'LCP : {lcp}', f'CLS: {cls}', sep='\n')