#!/usr/bin/env python
"""Usage: python flickr_crawler.py TAGS
TAGS is a space delimited list of tags

Created by Shuai Chen on 2017-06-08
Credit to Matt Warren of HalOtis
"""
__author__ = "Shuai Chen <shuaic92@gmail.com>"
__version__ = "$Rev: 3 $"
__date__ = "$Date: 2017-06-18 10:00:00 +0000 (Sun, 18 Jun 2017) $"
__copyright__ = "Copyright: 2017-8 Shuai Chen"

import sys
import shutil
import urllib
import flickr
 
NUMBER_OF_IMAGES = 100
 
#this is slow
def get_urls_for_tags(tags, number):
    photos = flickr.photos_search(tags=tags, tag_mode='all', per_page=number)
    urls = []
    for photo in photos:
        try:
            # size : size of photo Thumbnail, Small,
            #               Medium, Large, Original
            urls.append(photo.getURL(size='Original', urlType='source'))
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
    print "get_urls_for_tags()"
    urls = get_urls_for_tags(tags, NUMBER_OF_IMAGES)
    print "download_images()"
    download_images(urls)
 
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
