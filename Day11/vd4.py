#vd4
import requests, json
from datetime import datetime, timedelta

url = 'http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8'

#TODO: Lay du lieu bang requests
data = requests.get(url).text
print(data)

# Parse du lieu thanh object
obj = json.loads(data)

# In ra cac moc thoi gian + nhiet do 
for item in obj['list']:
    #print(json.dumps(item, indent=2))
    temp = item['main']['temp']
    date = item['dt_txt']
    date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') + timedelta(hours=7)
    date = date.strftime('%d/%m/%Y %H:%M:%S')
    print(f'Nhiệt độ lúc {date} : {temp} độ C')
