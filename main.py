import multiprocessing as mp
import time
import requests
import arggs

url = arggs.arg().ip
wordlist = arggs.arg().w

with open(wordlist, 'r') as wordlist:
    lines = wordlist.readlines()
    print(type(lines))


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

    for line in lines:
        line = line.rstrip()
        p1 = mp.Process(target=find, args=(line,))

        p1.start()

    end = time.time()

    r = end - start
    print(r)
