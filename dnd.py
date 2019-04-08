'''
    Do not distract yourself again!
    Simplistic script that add distracting
    websites (e.g. social media) to /etc/hosts

    usage: Disable distracting websites by adding them to /etc/hosts

    optional arguments:
      -h, --help  show this help message and exit
      -e          Enable protection from distrations
      -d          Disable protection from distrations
      -b          Backup /etc/hosts

      Author: Marios Papachristou
'''
import re
import argparse
import shutil


def get_hosts(delim='\n'):
    return delim.join([redirect + '\t' + url for url in distractions])


def backup():
    ''' Backup /etc/hosts '''
    shutil.copyfile('/etc/hosts', '/etc/hosts.bak')
    print('/etc/hosts was backed up successfully')


def enable():
    ''' Enable dnd.py '''
    with open('/etc/hosts', 'r') as f:
        contents = f.read()

    new_contents = '{}\n{}'.format(get_hosts(), contents)

    with open('/etc/hosts', 'w') as f:
        f.write(new_contents)

    print('Success! Go to work now!')


def disable():
    ''' Disable dnd.py '''
    with open('/etc/hosts', 'r') as f:
        contents = f.read()

    regex = get_hosts(delim='\n|')

    new_contents = re.sub(regex, '', contents).lstrip('\n')

    with open('/etc/hosts', 'w') as f:
        f.write(new_contents)

    print('Get ready to be distracted again!')


''' List of distractive websites '''
distractions = [
    'facebook.com',
    'www.facebook.com',
    'youtube.com',
    'www.youtube.com',
    'instagram.com',
    'www.instagram.com',
    'twitter.com',
    'www.twitter.com',
    'reddit.com',
    'www.reddit.com'
]

''' Where to redirect them '''
redirect = '127.0.0.1'

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        usage='Disable distracting websites by adding them to /etc/hosts')
    argparser.add_argument(
        '-e',
        help='Enable protection from distrations',
        action='store_true')
    argparser.add_argument(
        '-d',
        help='Disable protection from distrations',
        action='store_true')
    argparser.add_argument('-b', help='Backup /etc/hosts', action='store_true')

    args = argparser.parse_args()

    assert(args.e ^ args.d ^ args.b)

    if args.b:
        backup()

    if args.e:
        enable()
    elif args.d:
        disable()
