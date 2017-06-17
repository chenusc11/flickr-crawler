__author__ = "Khosrow Ebrahimpour <khosrow.ebrahimpour@gmail.com>"
__version__ = "$Rev: 3 $"
__date__ = "$Date: 2010-10-31 19:05:46 +0400 (Sun, 31 Oct 2010) $"
__copyright__ = "Copyright 2010 Khosorw Ebrahimpour"


import httplib
import mimetypes
import flickr
from xml.dom import minidom

		
def upload(self,filename, **params):
	#x = flickr._prepare_params(params)
	#args['api_key'] = self.__api_key 
	args = params
	sig = flickr._get_api_sig(params=params)

	args['api_key'] = flickr.API_KEY
	args['api_sig'] = sig
	args['auth_token'] = flickr.userToken()
	
	f = file(filename, 'rb')
	photo_data = f.read()
	f.close()
			
	# now make a "files" array to pass to uploader
	files = [('photo', filename, photo_data)]
	response = post_multipart('api.flickr.com', '/services/upload/', args, files)
	
	# use get data since error checking is handled by it already
	data = flickr._get_data(minidom.parseString(response))
	photo = flickr.Photo(data.rsp.photoid.text)
		
	return photo


"""
Code for post_multipart, encode_multipart_formdata, and get_content_type taken from
http://code.activestate.com/recipes/146306-http-client-to-post-using-multipartform-data/
PSF Licensed code
"""
		
def post_multipart(host, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """

    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields.items():
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)

	
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body
       
def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
    
    
if __name__ == '__main__':
	# the code below is an example of how to do an upload
	# please use it as a guide only
	photo = upload(filename='image.jpg', title='some photo', tags='tag1 tag2', description='A test photo')	

	print "your photo is now at : %s" % photo.getURL()

	 
    

