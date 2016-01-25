#!/usr/bin/python
"""updating the user details"""
import MySQLdb
import cgi
import cgitb 
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# connect to database
db = MySQLdb.connect("localhost","user1","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
gender = form.getvalue('gender')
date_of_birth = form.getvalue('date_of_birth')
contact_number = form.getvalue('contact_number')
email = form.getvalue('email')
username = form.getvalue('username')
password = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<br>{0}'.format(email)

user_id=0
try:
    sql_select = "SELECT user_detail_id FROM user_detail WHERE username = '{0}'".format(username)
    cursor.execute(sql_select)
    user_id = cursor.fetchone()

except:
    print "<br>Error"

try:
    sql_update = "UPDATE user_detail SET first_name='{0}',last_name='{1}',\
     gender='{2}',date_of_birth='{3}',contact_number='{4}',email='{5}',username='{6}',\
     password='{7}' WHERE user_detail_id = {8}"\
     .format(first_name,last_name,gender,date_of_birth,contact_number,email,username,password,user_id)
    cursor.execute(sql_update)
    db.commit()
    print """<br>Successfully updated please <a href="http://localhost/cgi-bin/task/login.html">login</a>again"""

except:
    print "<br>error in editing"
    db.rollback()


print '</body>'
print '</html>'

# close the mysql database connection
db.close()