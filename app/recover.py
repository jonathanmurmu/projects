#!/usr/bin/python
"""sends a recovery email containing the username and password to the given email address"""
import smtplib
import MySQLdb
import cgi, cgitb 
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

db = MySQLdb.connect("localhost","user1","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()
to=form.getvalue('email')
# sender username and password
sender = 'jonathan.murmu@mindfiresolutions.com'
sender_password = 'jono0077'

subject = 'Password Recovery Email'
# credentials of the user who forgot the username and password
username = ''
password = ''

print "Content-type:text/html\r\n\r\n"
print
print '<html>'
print '<head>'
print '<title>Recovery</title>'
print '</head>'
print '<body>'

# checks whether the emails is of the valid user already having an account
sql="SELECT IF( EXISTS(SELECT user_detail_id FROM user_detail WHERE email='{0}') ,1,0)".format(to)
cursor.execute(sql)
data=cursor.fetchone()
data=data[0]  # converting tuple to int, as fetchone() returned a tuple
# if the email does exits send the username and password to the given email
if data==1:

    try:
        cursor.execute("SELECT username,password FROM user_detail where email='{0}'".format(to))
        for row in cursor.fetchall():
            username = row[0]
            password = row[1]

        text = """username = {0} \r\npassword = {1}""".format(username,password)
        server = smtplib.SMTP('email.mindfiresolutions.com',587)
        server.ehlo()
        server.starttls()
        server.login(sender,sender_password)
        # compose the email
        body = '\r\n'.join([
                'To: {0}'.format(to),
                'From: {0}'.format(sender),
                'Subject: {0}'.format(subject), 
                '',
                text
                ])

        try:
            server.sendmail(sender,[to],body)
            print '<h3>Username and password is sent to your email address</h3>'
        except Exception as e:
            # print '<h3>Error sending email</h3>'
            line = open('../static/html_data/forgot_error.txt')
            print ''.join(line).format(to,e)

    except Exception as e:
        # print "<h3>Error</h3>"
        line = open('../static/html_data/forgot_error.txt')
        print ''.join(line).format(to,e)

    server.quit()

else:
    # print '<h3>Email does not exists..!</h3>'
    line = open('../static/html_data/forgot_error.txt')
    print ''.join(line).format(to,"Email does not exists")

db.close()
print "</body>"
print "</html>"
