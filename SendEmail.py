import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("prashantshastri@gmail.com","Data@300password")
server.sendmail(from_addr="prashantshastri@gmail.com",to_addrs="parth.mundhwa.com",msg="hello")
server.quit()


