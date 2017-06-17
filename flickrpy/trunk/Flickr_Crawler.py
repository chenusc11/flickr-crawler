#!/usr/bin/env python
"""Usage: python flickrDownload.py TAGS
TAGS is a space delimited list of tags
 
Created by Matt Warren on 2009-09-08.
Copyright (c) 2009 HalOtis.com. All rights reserved.
"""
import sys
import shutil
import urllib
 
import flickr
 
NUMBER_OF_IMAGES = 2
 
#this is slow
def get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, tag_mode='all', per_page=number)
    urls = []
    for photo in photos:
        try:
            urls.append(photo.getURL(size='Large', urlType='source'))
        except:
            continue
    return urls
 
def download_images(urls):
    for url in urls:
        file, mime = urllib.urlretrieve(url)
        name = url.split('/')[-1]
        print name
        shutil.copy(file, './'+name)
 
def main(*argv):
    args = argv[1:]
    if len(args) == 0:
        print "You must specify at least one tag"
        return 1
 
    tags = [item for item in args]
 
    urls = get_urls_for_tags(tags, NUMBER_OF_IMAGES)
    download_images(urls)
 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))