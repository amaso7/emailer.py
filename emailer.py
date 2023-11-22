import smtplib
from email.mime.text import MIMEText

def send_email(recipient, subject, body, email, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = recipient

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, password)
        server.sendmail(email, recipient, msg.as_string())
        server.close()
        print('Email sent successfully to', recipient)
    except Exception as e:
        print('Failed to send email:', e)

def main():
    email = input("Enter your Gmail address: ")
    password = input("Enter your Gmail password: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")
    recipient_input = input("Enter recipient email addresses separated by commas: ")
    recipients = [recipient.strip() for recipient in recipient_input.split(',')]

    for recipient in recipients:
        send_email(recipient, subject, body, email, password)

if __name__ == '__main__':
    main()
