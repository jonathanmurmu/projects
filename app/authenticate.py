#!/usr/bin/python
"""authenticate the user and opens the profile of the user if the login is successfull.
otherwise notify that is his accout is not active if he the authorised user with an inactive account.
And also display error message for wrong username and password """
import MySQLdb
import cgi
import cgitb
# Create instance of FieldStorage 
form = cgi.FieldStorage()
# connect to the database
db = MySQLdb.connect("localhost","user1","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()

txt_username = form.getvalue('username')
txt_password = form.getvalue('password')
print "Content-type:text/html\r\n\r\n"
print
try:

    sql_query1 = "SELECT user_detail_id FROM user_detail where username = '{0}' and password = '{1}'".format(txt_username,txt_password)
    cursor.execute(sql_query1)

    if cursor.fetchone():

        sql_query2="SELECT user_detail_id FROM user_detail where status='active' and username='{0}'".format(txt_username)
        cursor.execute(sql_query2)
        
        if cursor.fetchone():
            
            line=open('../static/html_data/files.text')
            try:
                sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,address_line_1,address_line_2,street,zip,contact_number,extra_note,mail,message,phone_call,other,email,username,user_detail_id,image_path\
                 FROM user_detail where username='{0}'".format(txt_username)
                
                cursor.execute(sql_display)
                
                for row in cursor.fetchall():
                    first_name = row[0]
                    last_name = row[1]
                    date_of_birth = row[2]
                    martial_status = row[3]
                    gender = row[4]
                    address_line_1 = row[5]
                    address_line_2 = row[6]
                    street = row[7]
                    zip_code = row [8]                  
                    contact_number = row[9]
                    extra_note = row[10]
                    mail = row[11]
                    message = row[12]
                    phone_call = row[13]
                    other = row[14]
                    email = row[15]
                    username = row[16]
                    user_detail_id = row[17]
                    image_path = row[18]
                
                if mail:
                    mail="mail"
                else:
                    mail=''
                if message:
                    message="message"
                else:
                    message=""
                if phone_call:
                    phone_call= "phone call"
                else:
                    phone_call=""
                if other:
                    other="other"
                else:
                    other=""

                print ''.join(line).format(first_name,last_name,date_of_birth,martial_status,gender,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,email,username,user_detail_id,image_path)

            except Exception as e:
                print
                print '<html>'
                print '<head>'
                print '<title>Login</title>'
                print '</head>'
                print '<body>'
                print '<h1>Oops!</h1>'
                print "<p>{0}</p>".format(e)  # error in fetching all the records from the database

        else:

            f=open('../static/html_data/login_error.text')
            tag='<div class="alert alert-danger">\
                    <strong>Error!</strong> Your account is not active. Please activate\
                </div>'
            print ''.join(f).format(tag)
    else:

        f=open('../static/html_data/login_error.text')
        tag='<div class="alert alert-danger">\
                    <strong>Error!</strong> Please Check..!\
                </div>'
        print ''.join(f).format(tag)
except Exception as e:
    f=open('../static/html_data/login_error.text')
    tag='<div class="alert alert-danger">\
            <strong>Error!</strong> {0}\
        </div>'.format(e)
    print ''.join(f).format(tag)

print '</body>'
print '</html>'

# close the mysql database connection
db.close()

