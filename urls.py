import re
import requests
import posixpath
import urlparse

SOURCE_URL = 'http://www.brandi.themefisher.com/'

with open('./index.html') as my_file:
    html = my_file.read()
    #urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
    urls = re.findall('(src|href)\=\"([^"]*)\"', html)

for u, path in urls:

    if 'http' not in path and any(x in path for x in ['jpg','png','css','js']):
      url = '%s%s' % (SOURCE_URL, path)
      print url
      response = requests.get(url)

      if not response.ok:
          # Something went wrong
          print "shit"
      else:

          with open('./assets/%s' % path, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
