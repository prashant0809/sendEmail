import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("prashantshastrikcsitglobal@gmail.com","Data@30071997")
server.sendmail(from_addr="prashantshastrikcsitglobal@gmail.com",to_addrs="parth.mundhwa@kcsitglobal.com",msg="hello")
server.quit()


