#!/usr/bin/env python

"""Simple Implementation of Snapchat Groups

Usage:
  brunonia.py -u <username> [-p <password> -q] -w <waittime>

Options:
  -h --help                 Show usage
  -q --quiet                Suppress output
  -u --username=<username>  Username
  -p --password=<password>  Password (optional, will prompt if omitted)
  -w --waittime=<period>    Sets period to check snaps (in seconds)

  Ex:

  python brunonia.py -u johndoe -p password -w 60

"""
from __future__ import print_function

import os.path
import os
import time
import sys
from getpass import getpass
from zipfile import is_zipfile, ZipFile

from docopt import docopt

from pysnap import get_file_extension, file_is_video, Snapchat

def process_snap(s, snap, path, quiet=False):
    filename = '{0}_{1}.{2}'.format(snap['sender'], snap['id'],
                                    get_file_extension(snap['media_type']))
    abspath = os.path.abspath(os.path.join(path, filename))
    if os.path.isfile(abspath):
        return
    data = s.get_blob(snap['id'])
    if data is None:
        return
    with open(abspath, 'wb') as f:
        f.write(data)
        if not quiet:
            print('Saved Snap to path: {0}'.format(abspath))


    if is_zipfile(abspath):
        zipped_snap = ZipFile(abspath)
        unzip_dir = os.path.join(path, '{0}_{1}'.format(snap['sender'],
                                                        snap['id']))
        zipped_snap.extractall(unzip_dir)
        if not quiet:
            print('Unzipped {0} to {1}'.format(filename, unzip_dir))
        postToBrunonia(filename, s)
    else:
        postToBrunonia(abspath, s)


def postToBrunonia(path, s):
    #actually set the story
    print('Posting ' + path + ' to ' + s.username + '...')
    video = file_is_video(path)
    media_id = s.upload(path)
    if media_id:
        print('Succesfully uploaded media (' + media_id + ')')    
    else:
        print('Could not upload media.')
        return -1
    if s.append_story(media_id, video, 10):
        print('Success!')
        return True
    else:
        print('Error: Could not update story.')
    

def main():
    arguments = docopt(__doc__)
    quiet = arguments['--quiet']
    username = arguments['--username']
    period = int(arguments['--waittime'])
    if arguments['--password'] is None:
        password = getpass('Password:')
    else:
        password = arguments['--password']
    
    s = Snapchat()
    if not s.login(username, password).get('logged'):
        print('Invalid username or password')
        sys.exit(1)

    print('Running Brunonia for ' + username + ' on directory ' + os.getcwd())
    while True:
        #fetching snaps
        print('Fetching snaps...')
        for snap in s.get_snaps():
            process_snap(s, snap, os.getcwd(), False)
        print('Waiting for ' + str(period) + ' seconds...')
        time.sleep(period)
    return 0
if __name__ == '__main__':
    main()
