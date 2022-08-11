import smtplib, ssl, getpass

class Email(object):
    def __init__(self):
        self.port = 465                             # SSL port
        self.smtp_server = "smtp.gmail.com"         # smtp server address
        creds = self.login_credentials()            # Sender credentials
        self.sender_email = creds["email"]          # Senders email
        self.password = creds["pass"]               # Senders password
        self.context = ssl.create_default_context() # Create a secure SSL context

    def login_credentials(self):
        """ The senders login credentials - password is hidden. """
        sender_email = str(input(r"Enter your email: "))
        password = getpass.getpass("Enter your password: ")
        return {"email":sender_email, "pass":password}

    def message(self):
        """ Subject and message content """
        subject = str(input(r"Subject: "))
        message = str(input(r"Message: "))
        return str(f"Subject: {subject}\n{message}")

    def send_mail(self):
        """ Email control and forwarding """
        receiver_email = str(input(r"Enter receivers email here: "))
        message = self.message()
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.port, context=self.context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message)
                print("\nEmail successfully sent!")
        except:
            print("\nError occurred while trying to send the email.. Please try again.")

if __name__ == "__main__":
    Email().send_mail()

