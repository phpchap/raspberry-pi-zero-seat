import requests
import json
import time

headers = {'content-type': 'application/json'}
url = 'https://b5kzdpasoc.execute-api.eu-west-1.amazonaws.com/production/sample_lambda'
data = {"page":"30"}
params = {"page":"30"}

print 'running file'

while True:
    print 'fetching latest'
    r = requests.post(url, params=params, data=json.dumps(data), headers=headers)
    f = open('text.json', 'w')
    f.write(r.text)
    print 'sleeping..'
    time.sleep(5)