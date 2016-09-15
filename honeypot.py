#!/usr/bin/env python
"""
YAHPOT: Yet Another Honey Pot is a HoneyPot and traffic logger 
written in Python, it can mimic webservers and other services.
 
Copyright (C) 2016 - jsacco@exploitpack.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time,socket,sys

def getConfig():
	banner = sys.argv[1]
	host = sys.argv[2]
	port = int(sys.argv[3])
	print "#"*36
	print "YahPot - HoneyPot and Traffic logger"
	print "#"*36
	if (port < 1) or (port > 65535):
		print 'Error: Invalid port number.'
		sys.exit();
	else:
		return (host, port, banner)

def writeLog(client, data=''):
	separator = '='*50
	fopen = open('./honey.log', 'a')
	fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, separator))
	fopen.close()

def newPot(host, port, banner):
	print 'Fake service listening on port: %s' % (port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, int(port)))
	s.listen(100)
	while True:
		(insock, address) = s.accept()
		print 'Connection received from: %s:%d' % (address[0], address[1])
		try:
			insock.send('%s\n'%(banner))
			data = insock.recv(1024)
			insock.close()
		except socket.error, e:
			writeLog(address)
		else:
			writeLog(address, data)
        
if __name__=='__main__':
	try:
		config = getConfig()
		newPot(config[0], config[1], config[2])
	except KeyboardInterrupt:
		print 'Closing..'
		exit(0)
	except BaseException, e:
		print 'Error: %s' % (e)
		exit(1)
