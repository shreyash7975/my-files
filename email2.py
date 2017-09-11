#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.uyash7975@gmail.com',587)
s.startls()
s.login("uyash7975@gmail.com","shreyash7975","")
message= "hello"
s.sendmail("uyash7975@gmail.com","uyash@79752gmail.com",message)
s.quit()s