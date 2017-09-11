#/usr/bin/python
import smtplib

try:
	server = smtp.SMTP('smtp.gmail.com',587)
 	server.ehlo()
 except:
 	print 'something went wrong...'
 	
 
