import multiprocessing as mp
import time

import requests

url = 'http://google.com'

with open('common.txt', 'r') as wordlist:
    lines = wordlist.readlines()


def find(lines):
    try:
        for line in lines:
            line = line.rstrip()
            dirs = requests.get(url + '/' + line)
            if dirs.status_code != 404:
                print(url + '/' + line)
            else:
                pass

    except:
        pass
time1 = time.time()
find(lines)
time2 = time.time()

res = time2 - time1

print(res)