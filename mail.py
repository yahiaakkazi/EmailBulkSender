from getpass import getpass
from utils.utils import get_contacts,read_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib

def main(contact = 'mycontacts.txt',message = 'message.txt'):
    host = str(input("Please type your host address "))
    port = input("ur port as well :) ")
    MY_ADDRESS = str(input("now ur mail address ! "))
    PASSWORD = getpass("Please type your mail password, no worries it will be invisible")
    civs, names, comps, emails  = get_contacts('mycontacts.txt') # read contacts
    message_template = read_template('message.txt')
    # set up the SMTP server
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    files = ["data/AKKAZI_Yahia_Certifications.pdf", "data/AKKAZI_Yahia_Resume_EN.pdf", "data/AKKAZI_Yahia_Resume_FR.pdf"]

    # For each contact, send the email:
    for civ, name, comp, email in zip(civs, names, comps, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title(),COMPANY = comp.title(),CIV = civ.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="Candidature spontanée pour un stage en Data"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        for f in files:  # add files to the message
            attachment = MIMEApplication(open(f, "rb").read(), _subtype="txt")
            attachment.add_header('Content-Disposition','attachment', filename=f)
            msg.attach(attachment)
        # send the message via the server set up earlier.
        s.send_message(msg)
        print("done")
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()