import argparse

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--v', nargs='?', help='Verbose mode', required=False)
    parser.add_argument('ip', help='Specify the ip address')
    parser.add_argument('-w', help='Specify the wordlist')
    args = parser.parse_args()

    return args

