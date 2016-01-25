#!/usr/bin/python
"""updates the address of the logged in user"""

import MySQLdb
import cgi
import cgitb
import re

form = cgi.FieldStorage()
# connect to the database
db = MySQLdb.connect("localhost","user1","mindfire","assignment")
# setup a cursor object using cursor() method
cursor = db.cursor()

user_detail_id = form.getvalue('user_detail_id')
address_line_1 = form.getvalue('address_line_1')
address_line_2 = form.getvalue('address_line_2')
street = form.getvalue('street')
zip_code = form.getvalue('zip')
contact_number = form.getvalue('contact_number')

print "Content-type:text/html\r\n\r\n"
print
print '<html>'
print '<head>'
print '<title>Edit Page</title>'
print '</head>'
print '<body>'

# validating contact number
phone_number = contact_number
p = re.compile('(^[0-9]{10}$)')
try:
    phone = p.match(phone_number)
except:
    phone = ''

# validating zip code
zip_number = zip_code
z = re.compile('(^[0-9]{6}$)')
try:
    zip_code_number = z.match(zip_number)
except:
    zip_code_number = ''

# displaying the error message and retaining the previous values of the input fields if the validation error occurs
if zip_code_number in [None, '', "N/A", 'NULL', 'None']:

    line = open("../static/html_data/editfile_error.txt")
    sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,\
    extra_note,mail,message,phone_call,other,image_path \
    FROM user_detail where user_detail_id='{0}'".format(user_detail_id)
    cursor.execute(sql_display)
    for row in cursor.fetchall():
        first_name = row[0]
        last_name = row[1]
        date_of_birth = row[2]
        martial_status = row[3]
        gender = row[4]
        extra_note = row[5]
        mail = row[6]
        message = row[7]
        phone_call = row[8]
        other = row[9]
        image_path = row[10]

    if martial_status=="single":
        single="selected"
    else:
        single=" "
    if martial_status=="married":
        married="selected"
    else:
        married=" "
    if gender=="male":
        male="checked"
    else:
        male=" "
    if gender=="female":
        female="checked"
    else:
        female=" "
    if mail==1:
        mail="checked"
    else:
        mail=" "
    if message==1:
        message="checked"
    else:
        message=" "
    if phone_call==1:
        phone_call="checked"
    else:
        phone_call=" "
    if other==1:
        other="checked"
    else:
        other= " "
    error_message = "Fill valid zip code"
    print ''.join(line).format(first_name,last_name,date_of_birth,single,married,male,female,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,user_detail_id,image_path,error_message)

elif phone in [None, '', "N/A", 'NULL','None']:

    line = open("../static/html_data/editfile_error.txt")
    sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,\
    extra_note,mail,message,phone_call,other,image_path \
    FROM user_detail where user_detail_id='{0}'".format(user_detail_id)
    cursor.execute(sql_display)
    for row in cursor.fetchall():
        first_name = row[0]
        last_name = row[1]
        date_of_birth = row[2]
        martial_status = row[3]
        gender = row[4]
        extra_note = row[5]
        mail = row[6]
        message = row[7]
        phone_call = row[8]
        other = row[9]
        image_path = row[10]

    if martial_status=="single":
        single="selected"
    else:
        single=" "
    if martial_status=="married":
        married="selected"
    else:
        married=" "
    if gender=="male":
        male="checked"
    else:
        male=" "
    if gender=="female":
        female="checked"
    else:
        female=" "
    if mail==1:
        mail="checked"
    else:
        mail=" "
    if message==1:
        message="checked"
    else:
        message=" "
    if phone_call==1:
        phone_call="checked"
    else:
        phone_call=" "
    if other==1:
        other="checked"
    else:
        other= " "
    error_message = "Fill valid contact number"
    print ''.join(line).format(first_name,last_name,date_of_birth,single,married,male,female,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,user_detail_id,image_path,error_message)


else:

    # updating the the address fields
    try:
        sql_status = "UPDATE user_detail SET address_line_1='{0}',address_line_2='{1}',street='{2}',zip='{3}',contact_number='{4}' where user_detail_id = {5}".format(address_line_1,address_line_2,street,zip_code,contact_number,user_detail_id)
        cursor.execute(sql_status)
        db.commit()

        line = open('../static/html_data/editfile.text')
        try:
            sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,address_line_1,address_line_2,street,zip,contact_number,extra_note,mail,message,phone_call,other,image_path FROM user_detail where user_detail_id='{0}'".format(user_detail_id)

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
                zip_code = row[8]
                contact_number = row[9]
                extra_note = row[10]
                mail = row[11]
                message = row[12]
                phone_call = row[13]
                other = row[14]
                image_path = row[15]

            if martial_status=="single":
                single="selected"
            else:
                single=" "
            if martial_status=="married":
                married="selected"
            else:
                married=" "

            if gender=="male":
                male="checked"
            else:
                male=" "
            if gender=="female":
                female="checked"
            else:
                female=" "

            if mail==1:
                mail="checked"
            else:
                mail=" "
            if message==1:
                message="checked"
            else:
                message=" "
            if phone_call==1:
                phone_call="checked"
            else:
                phone_call=" "
            if other==1:
                other="checked"
            else:
                other= " "

            print ''.join(line).format(first_name,last_name,date_of_birth,single,married,male,female,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,user_detail_id,image_path)

        except:

            line = open("../static/html_data/editfile_error.txt")
            sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,\
            extra_note,mail,message,phone_call,other,image_path \
            FROM user_detail where user_detail_id='{0}'".format(user_detail_id)
            cursor.execute(sql_display)
            for row in cursor.fetchall():
                first_name = row[0]
                last_name = row[1]
                date_of_birth = row[2]
                martial_status = row[3]
                gender = row[4]
                extra_note = row[5]
                mail = row[6]
                message = row[7]
                phone_call = row[8]
                other = row[9]
                image_path = row[10]

            if martial_status=="single":
                single="selected"
            else:
                single=" "
            if martial_status=="married":
                married="selected"
            else:
                married=" "
            if gender=="male":
                male="checked"
            else:
                male=" "
            if gender=="female":
                female="checked"
            else:
                female=" "
            if mail==1:
                mail="checked"
            else:
                mail=" "
            if message==1:
                message="checked"
            else:
                message=" "
            if phone_call==1:
                phone_call="checked"
            else:
                phone_call=" "
            if other==1:
                other="checked"
            else:
                other= " "
            error_message = "Connection problem"
            print ''.join(line).format(first_name,last_name,date_of_birth,single,married,male,female,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,user_detail_id,image_path,error_message)

    except:

        db.rollback()
        line = open("../static/html_data/editfile_error.txt")
        sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,gender,\
        extra_note,mail,message,phone_call,other,image_path \
        FROM user_detail where user_detail_id='{0}'".format(user_detail_id)
        cursor.execute(sql_display)
        for row in cursor.fetchall():
            first_name = row[0]
            last_name = row[1]
            date_of_birth = row[2]
            martial_status = row[3]
            gender = row[4]
            extra_note = row[5]
            mail = row[6]
            message = row[7]
            phone_call = row[8]
            other = row[9]
            image_path = row[10]
        if martial_status=="single":
            single="selected"
        else:
            single=" "
        if martial_status=="married":
            married="selected"
        else:
            married=" "
        if gender=="male":
            male="checked"
        else:
            male=" "
        if gender=="female":
            female="checked"
        else:
            female=" "
        if mail==1:
            mail="checked"
        else:
            mail=" "
        if message==1:
            message="checked"
        else:
            message=" "
        if phone_call==1:
            phone_call="checked"
        else:
            phone_call=" "
        if other==1:
            other="checked"
        else:
            other= " "
        error_message = "Error in Updation"
        print ''.join(line).format(first_name,last_name,date_of_birth,single,married,male,female,address_line_1,address_line_2,street,zip_code,contact_number,extra_note,mail,message,phone_call,other,user_detail_id,image_path,error_message)

print '</body>'
print '</html>'

# close the mysql database connection
db.close()
