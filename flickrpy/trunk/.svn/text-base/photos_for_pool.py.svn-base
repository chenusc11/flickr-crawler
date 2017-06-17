#!/usr/bin/python
"""Usage: python photos_for_pool.py [OPTIONS] group_id
group_id must the flickr NSID for a group

OPTIONS:
  -v or --verbose
  -e or --equal : width and height of photo must be the same
  -s size or --size size : size of photo Thumbnail, Small,
                           Medium, Large, Original
  -n number or --number number : the number of photos to retrieve

"""


__author__ = "James Clarke <james@jamesclarke.info>"
__version__ = "$Rev$"
__date__ = "$Date$"
__copyright__ = "Copyright 2004-5 James Clarke"

import sys
import urllib
import flickr

verbose = False

def getURL(photo, size, equal=False):
    """Retrieves a url for the photo.  (flickr.photos.getSizes)
    
    photo - the photo
    size - what size 'Thumbnail, Small, Medium, Large, Original'
    equal - should width == height?
    """
    method = 'flickr.photos.getSizes'
    data = flickr._doget(method, photo_id=photo.id)
    for psize in data.rsp.sizes.size:
        if psize.label == size:
            if equal and psize.width == psize.height:
                return psize.source
            elif not equal:
                return psize.source
    raise flickr.FlickrError, "No URL found"

def getPhotoURLs(groupid, size, number, equal=False):
    group = flickr.Group(groupid)
    photos = group.getPhotos(per_page=number)
    urls = []
    for photo in photos:
        try:
            urls.append(getURL(photo, size, equal))
        except flickr.FlickrError:
            if verbose:
                print "%s has no URL for %s" % (photo, size)
    return urls
    

def main(*argv):
    from getopt import getopt, GetoptError

    try:
        (opts, args) = getopt(argv[1:],\
                              'ves:n:',\
                              ['verbose', 'size', 'equal', 'number'])
    except GetoptError, e:
        print e
        print __doc__
        return 1

    size = 'Medium'
    equal = False
    number = 100
    
    for o, a in opts:
        if o in ('-s' , '--size'):
            size = a.capitalize()
        elif o in ('-e', '--equal'):
            equal = True
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-n', '--number'):
            number = a
        else:
            print "Unknown argument: %s" % o
            print __doc__
            return 1
        
    if len(args) == 0:
        print "You must specify a group"
        print __doc__
        return 1
    
    groupid = args[0]
    
    urls = getPhotoURLs(groupid, size, number, equal)

    for url in urls:
        print url
        
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
