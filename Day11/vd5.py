#vd5 : dich vu OCR cua Google vision
import requests, json, base64  

url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyA8It5i51gkaMFan9ZzFW4MurmsuNKfxU4'

def docVanBan(file):
    with open(file, 'rb') as f:
        img = f.read()
        img_base64 = base64.b64encode(img)
        
    body = {"requests": [
        {
            "image": {"content" : img_base64.decode("utf-8")},
            "features": [{"type": "DOCUMENT_TEXT_DETECTION"}]
            }
        ]}

    req = requests.post(url, data = json.dumps(body))
    
    with open('response.json','w', encoding='utf-8') as fo:
        fo.write(req.text)

    obj = json.loads(req.text)
    return obj['responses'][0]['fullTextAnnotation']['text']

print(docVanBan('sample.jpg'))