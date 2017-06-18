#!/usr/bin/python
"""Usage: python wallpaper.py [OPTIONS] TAGS
TAGS is a space delimited list of tags

OPTIONS:
  -w screenwidth or --width screenwidth
  -h screenheight or --height screenheight
  -f filename or --file filename

Requires:
 - Python Imaging Library [http://www.pythonware.com/products/pil/]
"""

__author__ = "Shuai Chen <shuaic92@gmail.com>, James Clarke <james@jamesclarke.info>"
__version__ = "$Rev: 3 $"
__date__ = "$Date: 2017-06-18 10:00:00 +0000 (Sun, 18 Jun 2017) $"
__copyright__ = "Copyright 2004-5 James Clarke, Portions: 2017 Shuai Chen"


import sys
import urllib
import math
import random
from PIL import Image
import flickr

#this is slow as so many API calls
def get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, per_page=number)
    urls = []
    for photo in photos:
        urls.append(photo.getURL(size='Square', urlType='source'))
    return urls

#quicker to just 'hack' the url
#I don't think this works anymore, a change in url format
def quick_get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, per_page=number)
    urls = []
    for photo in photos:
        urls.append('http://photos%s.flickr.com/%s_%s_s.jpg' %\
                    (photo.server, photo.id, photo.secret))
    return urls

def photos_required(screen, size=(100, 100)):
    """screen is tuple (width, height)"""
    width = int(math.ceil(float(screen[0]) / size[0]))
    height = int(math.ceil(float(screen[1]) / size[1]))
    return width * height

def create_wallpaper(screen, urls, size=(100, 100), randomise=False):
    if randomise:
        random.shuffle(urls)

    wallpaper = Image.new("RGB", screen, "blue")

    width = int(math.ceil(float(screen[0]) / size[0]))
    height = int(math.ceil(float(screen[1]) / size[1]))
    
    offset = [0,0]
    for i in xrange(height):
        y = size[1] * i
        for j in xrange(width):
            x = size[0] * j
            photo = load_photo(urls.pop())
            if photo.size != size:
                photo = photo.resize(size, Image.BICUBIC)
            wallpaper.paste(photo, (x, y))
            del photo
    return wallpaper
        

def load_photo(url):
    file, mime = urllib.urlretrieve(url)
    photo = Image.open(file)
    return photo

def main(*argv):
    from getopt import getopt, GetoptError

    try:
        (opts, args) = getopt(argv[1:], 'w:h:f:', ['width', 'height', 'file'])
    except GetoptError, e:
        print e
        print __doc__
        return 1

    width = 100
    height = 100
    file = 'wallpaper.jpg'
    
    for o, a in opts:
        if o in ('-w', '--width'):
            width = int(a)
        elif o in ('-h', '--height'):
            height = int(a)
        elif o in ('-f' '--file'):
            file = a
        else:
            print "Unknown argument: %s" % o
            print __doc__
            return 1
        
    if len(args) == 0:
        print "You must specify at least one tag"
        print __doc__
        return 1
    
    tags = [item for item in args]
    
    screen = (width, height)

    print "photos_required()"
    n = photos_required(screen)
    print "get_urls_for_tags()"
    urls = get_urls_for_tags(tags, n)
    print "create_wallpaper()"
    wallpaper = create_wallpaper(screen, urls, randomise=True)
    print "save()"
    wallpaper.save(file)

if __name__ == '__main__':
    sys.exit(main(*sys.argv))
