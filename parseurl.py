#!/bin/python

# exmaple 1: parse a url with re module
# this take a string with a url and split the protocol, ip or nameserver and port
# if port don't exist and the protocol is http the port is 80.

import re

url = raw_input('url : ')

# check if the url has the form protocol://hostname:port
# protocol is character set [a-zA-Z]{3,} ftp, http, mongodb, ssh, etc.
# hostname is character set [a-zA-Z0-9\\.\-] www.server.com, 127.0.0.1, etc.
# port is numeric [0-9] 80, 8080, 21, 22, 25, 27001, etc. If you omit the port, assume 80 if protocol is http.
# ToDO:
# - If protocol is ftp and you omit the port, set port number 21
# - If protocol is ssh and you omit the port, set port number 22
# Etc...

parser = re.compile('[a-zA-Z]{2,}://[a-zA-Z0-9\\.\-]+(?::[0-9]{2,}|:?)$')

if bool(parser.search(url)):
     print 'The url is valid << %s >>'%url
     protocol = re.search('\w+(?=://)',url).group()
     hostname = re.search('(?<=://)[a-zA-Z0-9\\.\-]+(?=:)*',url).group()
     port     = re.search('(?<=:)[0-9]{2,}',url)  
     print protocol
     print hostname
     if port != None:
          print port.group()
     else:
	  if protocol == 'http': print '80'
else:
     print 'The url is invalid << %s >>'%url

