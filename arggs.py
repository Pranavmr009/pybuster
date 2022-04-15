import argparse


def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--v', nargs='?', help='Verbose mode', required=False)
    parser.add_argument('ip', help='Specify the ip address')
    parser.add_argument('-w', help='Specify the wordlist')
    args = parser.parse_args()

    return args

# print(arg().ip)

# if 'v' in args:
#     print('YES')
#
# def get_url():
#     arg = args.ip
#     print(arg)
#
# def get_wordlist():
#     arg = args.w
#     print(arg)
#
# print(args.v)
# get_url()
# get_wordlist()

# if args.v:
#     print('VERRR')
# if args.verbose == '10':
#     print(args.verbose)
#
# elif args.host == '11':
#     print(args.host)
