import multiprocessing as mp
import time
import requests
import arggs
import sys
from datetime import date, datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
today = date.today()
url = arggs.arg().ip
wordlist = arggs.arg().w
user_agent = requests.utils.default_headers()
google_url = 'http://www.google.com'

try:
    print('Checking your internet connection..........')
    r = requests.get(google_url)
    print('You are connected')

except:
    print('Something wrong with your connection! Please try again!!')
    sys.exit()

try:
    r1 = requests.get(url)

except:
    print('Something wrong with the url!! exiting!!!')
    sys.exit()


def find(line):
    try:
        # for line in lines:
        #     line = line.rstrip()
        dirs = requests.get(url + '/' + line)
        if dirs.status_code != 404:
            print(f"{url}/{line}                                   (status: {dirs.status_code})")
        else:
            pass

    except:
        pass


if __name__ == '__main__':

    start = time.time()
    try:
        print(f"""
        
=============================================================================================
Pybuster v1.0.0
by PRANAV MR, 2022
==============================================================================================
Url:                    {url}
Method:                 GET
Wordlist:               {wordlist}
Negative status code:   404
User Agent:             {user_agent['User-Agent']}
==============================================================================================
{today} {current_time} Starting Pybuster enumerating directories
===============================================================================================
        """)
        with open(wordlist, 'r') as wordlist:
            lines = wordlist.readlines()

        for line in lines:
            line = line.rstrip()
            p1 = mp.Process(target=find, args=(line,))

            p1.start()

        end = time.time()

        r = end - start
        print(r)

        print(f"""
===============================================================================================
{today} {current_time} Finished
===============================================================================================
""")

    except FileNotFoundError:
        print('File not in path')
