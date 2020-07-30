import requests
url = 'http://127.0.0.1:5000/results'
data = {'conam':'1000', 'contp':'0', 'ecfg':'1',
'etymd':'0','flbmk':'2','hcefg':'3','ovrlt':'0',
'stscd':'2','month':'1','loctm_hour':'9'}
response1 = requests.post(url, data=data)
response1.json()