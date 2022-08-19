from getpass import getpass
from utils.utils import get_contacts,read_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def main(contact = 'mycontacts.txt',message = 'message.txt'):
    host = str(input("Please type your host address "))
    port = input("ur port as well :) ")
    MY_ADDRESS = str(input("now ur mail address ! "))
    PASSWORD = getpass("Please type your mail password, no worries it will be invisible")
    names, emails = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')
    # set up the SMTP server
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is TEST"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
        # s.send_message(msg)
        print("done")
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()