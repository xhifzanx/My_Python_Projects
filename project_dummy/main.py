import smtplib

my_email = "dummyacounhotmail@gmail.com"
password = "hifzan1234"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="misterj435@gmail.com", msg="hello")
connection.close()