# Goi service dịch của Google
import requests, json
url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyA8It5i51gkaMFan9ZzFW4MurmsuNKfxU4'

body = {
    "q": "clear sky",
    "source": "en",
    "target": "vi",
    "format": "text"
}
result = requests.post(url, data=json.dumps(body)).text
#print(result)

obj = json.loads(result)
print(obj['data']['translations'][0]['translatedText'])