import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("uyash7975@gmail.com", "classified information")
 
msg = "hello"
server.sendmail("uyash7975@gmail.com", "uyash7975@gmail.com", msg)
server.quit()
