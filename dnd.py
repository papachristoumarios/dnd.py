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
      -i          Time interval to protect (in minutes)
      Author: Marios Papachristou
'''
import re
import argparse
import shutil
import time
import datetime

def get_hosts(delim='\n'):
    return delim.join([redirect + '\t' + url for url in distractions])


def restore():
    ''' Restore /etc/hosts '''
    shutil.copyfile('/etc/hosts.bak', '/etc/hosts')
    print('/etc/hosts was restored successfully')


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
    argparser.add_argument('-r', help='Restore /etc/hosts', action='store_true')

    group = argparser.add_mutually_exclusive_group()
    group.add_argument('-t', help='Time interval to protect you (in minutes)', type=float)
    group.add_argument('-u', help='Protect until the specified time', type=str)

    args = argparser.parse_args()

    assert(args.e ^ args.d ^ args.b ^ args.r)

    if args.b:
        backup()

    if args.r:
        restore()

    if args.e:
        enable()
    elif args.d:
        disable()
    
    if args.t != None and (args.e ^ args.d):
        assert(args.t >= 0)
        time.sleep(args.t * 60)
        if args.e:
            disable()
        else:
            enable()

    if args.u != None and (args.e ^ args.d):
        currentTime = datetime.datetime.now()
        cy, cm, cd = currentTime.year, currentTime.month, currentTime.day
        eh, emin = map(int, args.u.split(':'))
        endTime = datetime.datetime(cy, cm, cd, eh, emin, 0)
        difference = (endTime - currentTime).total_seconds()
        assert(difference > 0)
        time.sleep(difference)
        if args.e:
            disable()
        else:
            enable()

