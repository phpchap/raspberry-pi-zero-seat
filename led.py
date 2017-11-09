import requests
import json
from pprint import pprint
import scrollphathd as sphd
import time
from uuid import getnode as get_mac

sphd.set_brightness(0.5)

while True:
    with open('text.json') as data_file:
        data = json.load(data_file)
        for key, value in data.items():
            v = value

    sphd.clear()
    sphd.write_string(v)
    sphd.show()
    sphd.scroll(1)
    pprint(v)
    print 'sleeping..'
    time.sleep(3)
    print 'updated..'