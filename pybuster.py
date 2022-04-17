import multiprocessing as mp
import time
import requests
import arggs
import sys

url = arggs.arg().ip
wordlist = arggs.arg().w

google_url = 'http://www.google.com'

try:
    r = requests.get(google_url)

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
            print(url + '/' + line)
        else:
            pass

    except:
        pass


if __name__ == '__main__':

    start = time.time()
    try:
        with open(wordlist, 'r') as wordlist:
            lines = wordlist.readlines()

        for line in lines:
            line = line.rstrip()
            p1 = mp.Process(target=find, args=(line,))

            p1.start()

        end = time.time()

        r = end - start
        print(r)

    except FileNotFoundError:
        print('File not in path')
