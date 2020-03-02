import matplotlib, csv, os, smtplib, ssl

port = 587 # This is for SSL
smtp_address = 'smtp.gmail.com' # Allows us to use gmail
my_address = 'gmaniscreepy03@gmail.com'
target_email = 'jdf435@humboldt.edu'

password = input("password: ")
message = """\
Subject: Late Status

Hello, {firstname}
This is to let you know that you have an item that is overdue.

Regards,
Jakob."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_address, port) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(my_address, password) #connects to google using your email and password

    with open('contacts.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for firstname, lastname, status, email in reader: #iterates through the csv file looking for given parameters

            if status == "late": 
                server.sendmail(my_address, email, message.format(firstname=firstname))
                print("Sending mail to: " + email)
            else:
                print("on time")
    server.quit()
    #Send the email



# if __name__ == '__main__':
#     execute_email()
