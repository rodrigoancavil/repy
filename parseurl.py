#!/bin/python

# exmaple 1: parse a url with re module
# this take a string with a url and split the protocol, ip or nameserver and port
# if port don't exist and the protocol is http the port is 80.

import re

url = raw_input('url : ')

# check if the url has the form protocol://hostname:port
# protocol is character set [a-zA-Z]
# hostname is character set [a-zA-Z0-9]
# port is numeric [0-9]

parser = re.compile('[a-zA-Z]{4,}://[a-zA-Z0-9\\.-]+:*[0-9]*')

if parser.match(url) != None:
     print 'The url is valid <<%s>>'%parser.match(url).group()
     protocol = re.search('\w+(?=://)',url).group()
     hostname = re.search('(?<=://)[a-zA-Z\\.-]+(?=:)*',url).group()
     port     = re.search('(?<=:)[0-9]{2,}',url)  
     print protocol
     print hostname
     if port != None:
          print port.group()
     else:
          print '80'
else:
     print 'The url is invalid <<%s>>'%url

