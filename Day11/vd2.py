# Lay du lieu tu webservice
import requests, json
url = 'https://api.openweathermap.org/data/2.5/weather?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9'
data = requests.get(url).text
obj = json.loads(data)
temp = obj['main']['temp']
print(f'Nhiệt độ Hà Nội hiện tại là {temp} độ C')
weather = obj['weather'][0]['description']
print('Thời tiết : ', weather)