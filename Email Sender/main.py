# import libs
from smtplib import SMTP
from email.mime.text import MIMEText
from random import choice
import password_manager
import morning_quotes as quotes
import datetime as dt

# Set email sending time
send_time = dt.datetime.now().strftime("%I : %M %p")
# Remove the zero
if send_time.startswith("0"):
    send_time = send_time[1:]

# Get random daily quotes
if send_time == "6 : 00 AM":
    daily_quotes = choice(quotes.morning_quotes)
    # #
    password = password_manager.password
    subject = "Hello Praveen Kumar Good Morning"
    body = f"""
    Hi Praveen,
    
    Good morning! ☀️ I hope today brings you a fresh start, new opportunities, and the energy to achieve all your goals! 💪✨
    
    Here’s a little boost of motivation to kickstart your day:
    
    {daily_quotes}
    
    """
    msg = MIMEText(body, "plain")
    msg['From'] = "pk9777066@gmail.com"
    msg["To"] = "praveentechci2023@gmail.com"
    msg["Subject"] = subject
    #
    # #
    with SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="pk9777066@gmail.com", password=password)
        connection.sendmail(from_addr="pk9777066@gmail.com",
                            to_addrs="jothiramanpraveen007@gmail.com",
                            msg=msg.as_string())
    print("Send Successfully")

