#!/usr/bin/python
"""Usage: python tags2set.py [OPTIONS] TAGS
TAGS is a space delimited list of tags

OPTIONS:
  -e address or --email address
  -p password or --password password
  -t title or --title title
  -d description or --description description  [optional]
  Enclose title and description in 'quotes' for multiple words
"""

__author__ = "James Clarke <james@jamesclarke.info>"
__version__ = "$Rev$"
__date__ = "$Date$"
__copyright__ = "Copyright 2004 James Clarke"

import sys
import flickr

def set_from_tags(tags, title, description, all=True):
    """all=True means include non-public photos"""
    user = flickr.test_login()
    photos = flickr.photos_search(user_id=user.id, auth=all, tags=tags)
    set = flickr.Photoset.create(photos[0], title, description)
    set.editPhotos(photos)
    return set

def main(*argv):
    from getopt import getopt, GetoptError

    try:
        (opts, args) = getopt(argv[1:], 'e:p:t:d:', \
                              ['email', 'password', 'title', 'description'])
    except GetoptError, e:
        print e
        print __doc__
        return 1

    title = None
    description = ''
    
    for o, a in opts:
        if o in ('-e', '--email'):
            flickr.email = a
        elif o in ('-p', '--password'):
            flickr.password = a
        elif o in ('-t', '--title'):
            title = a
        elif o in ('-d', '--description'):
            description = a
        else:
            print "Unknown argument: %s" % o
            print __doc__
            return 1

    if flickr.email is None:
        print "email is required"
        print __doc__
        return 1
    if flickr.password is None:
        print "password is required"
        print __doc__
        return 1
    if title is None:
        print "title is required"
        print __doc__
        return 1
    if len(args) == 0:
        print "You must specify at least one tag"
        print __doc__
        return 1
    
    tags = [item for item in args]

    set = set_from_tags(tags, title, description)
    print "Photoset %s created with %s photos" % (set.title, len(set)) 
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
    
