# Lay noi dung website
import requests

url = 'https://google.com'

html = requests.get(url).text

with open('google.html', 'w', encoding='utf-8') as f:
    f.write(html)
    