#!/usr/bin/python
"""Registers the new user and send an activation email to the user"""

import MySQLdb
import cgi, cgitb
import smtplib
import datetime
import re
from email.utils import parseaddr
from validate_email import validate_email

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# connect to the database
db = MySQLdb.connect("localhost","user1","mindfire","assignment")
# setup a cursor object using cursor() method
cursor = db.cursor()

password = form.getvalue('password')
confirm_password = form.getvalue('confirm_password')
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
gender = form.getvalue('gender')
date_of_birth = form.getvalue('date_of_birth')
contact_number = form.getvalue('contact_number')
email = form.getvalue('email')
username = form.getvalue('username')
date = "false"

print "Content-type:text/html\r\n\r\n"
print
print '<html>'
print '<head>'
print '<title>Registration</title>'
print '</head>'
print '<body>'

# validating date
try:
    datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
    date = 'true'
except:
    date = 'false'

# validating contact number
phone_number = contact_number
p = re.compile('(^[0-9]{10}$)')
try:
    phone = p.match(phone_number)
except:
    phone = ''

# email validation
try:
    email_address = validate_email(email,verify=True)
except:
    email_address = 'False'
# displaying the appropriate error messages
if first_name in [None, '', "N/A", 'NULL','None']:
    message = "Please fill first name"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif last_name in [None, '', "N/A", 'NULL','None']:
    message = "Please fill last name"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif gender in [None, '', "N/A", 'NULL','None']:
    message = "Please select gender name"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif date_of_birth in [None, '', "N/A", 'NULL','None']:
    message = "Please enter date in YYYY-MM-DD"
    line = open("../static/html_data/register_error.txt")
    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""
    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif date == 'false':
    message = "Please enter date in YYYY-MM-DD"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""
    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif phone in [None, '', "N/A", 'NULL','None']:
    message = "Please enter valid contact number"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif email in [None, '', "N/A", 'NULL', 'None']:
    message = "Please enter email"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif email_address in [None, '', "N/A", 'NULL', 'None',False]:
    message = "Please enter valid email"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif username in [None, '', "N/A", 'NULL','None']:
    message = "Please enter username"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif password in [None, '', "N/A", 'NULL','None']:
    message = "Please enter password"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

elif confirm_password in [None, '', "N/A", 'NULL','None']:
    message = "Please enter confirm password"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)


# if both the passwords the match then details will be saved in the data base
elif password == confirm_password:

    try:
        sql="INSERT INTO user_detail(first_name,last_name,gender,date_of_birth,contact_number,email,username,password,status)\
         VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','inactive')"\
         .format(first_name,last_name,gender,date_of_birth,contact_number,email,username,password)
        cursor.execute(sql)
        db.commit()

        # retreiveing the id of the user and sending activation link in email
        try:
            cursor_id = db.cursor()
            sql_id = "SELECT user_detail_id FROM user_detail where username = '{0}'".format(username)
            cursor_id.execute(sql_id)
            user_id_tuple = cursor_id.fetchone()

            # converting tuple into int as user_id is a tuple now
            for user_id in user_id_tuple:
                pass

            # sending activation link through email
            to = '{0}'.format(email)
            sender = 'jonathan.murmu@mindfiresolutions.com'
            sender_password = 'jono0077'
            subject = 'Activation Email'
            # writing the email content to send
            text="""Click this link to activate your account

                    <a href="http://localhost/cgi-bin/projects/task/app/activate.py?id={0}">link</a>
                    """.format(user_id)

            server = smtplib.SMTP('email.mindfiresolutions.com',587)
            server.ehlo()
            server.starttls()
            server.login(sender,sender_password)
            # composing the email
            body = '\r\n'.join([
                    'To: {0}'.format(email),
                    'From: {0}'.format(sender),
                    'Subject: {0}'.format(subject),
                    'MIME-Version: 1.0',
                    'Content-type: text/html'
                    '',
                    text
                    ])

            try:
                server.sendmail(sender,[to],body)
                print '<p>An activation link has been sent to your email address</p>'
            except Exception as e:
                # email sending error
                message = e
                line = open("../static/html_data/register_error.txt")

                if gender == "male":
                    male = "checked"
                else:
                    male = ""
                if gender == "female":
                    female = "checked"
                else:
                    female = ""

                print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

            server.quit()
            # sending email end

        except Exception as e:
            # display "Registration failed !"
            message = e
            line = open("../static/html_data/register_error.txt")

            if gender == "male":
                male = "checked"
            else:
                male = ""
            if gender == "female":
                female = "checked"
            else:
                female = ""

            print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

    except Exception as e:
        db.rollback()
        # display "Registration failed"
        message = e
        line = open("../static/html_data/register_error.txt")

        if gender == "male":
            male = "checked"
        else:
            male = ""
        if gender == "female":
            female = "checked"
        else:
            female = ""

        print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

else:
    # print "Password didnt match"
    message = "Password did not match"
    line = open("../static/html_data/register_error.txt")

    if gender == "male":
        male = "checked"
    else:
        male = ""
    if gender == "female":
        female = "checked"
    else:
        female = ""

    print ''.join(line).format(first_name, last_name, male, female, date_of_birth, contact_number, email, username, password, confirm_password, message)

print '</body>'
print '</html>'

# close the mysql database connection
db.close()
