import requests
import time
import random

while True:
    print('Sending data to ThingSpeak')
    data = random.randint(0, 200)
    URL = 'https://api.thingspeak.com/update?api_key=PDMSVQEHEWRAAD5K&field1='+str(data)
    r = requests.get(URL)
    print(r)
    print(data)
    time.sleep(15)

