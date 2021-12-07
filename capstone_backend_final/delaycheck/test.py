import requests
import json
import time

url_items = "http://192.168.50.94:8000/Vehicle/Battery"

delay_list = []
msg_idx = [i for i in range(1,101)]

idx = 0
while idx < 100:
    time_before = time.time()
    response = requests.get(url_items)
    print(response.text)
    time_after = time.time()
    delay = time_after - time_before
    msg_idx.append(delay)
    print(str(idx) + ": "+str(delay))
    print("\n")
    idx += 1
    time.sleep(1)
    