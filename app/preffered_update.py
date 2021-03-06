#!/usr/bin/python
"""Updating the preffered communication medium of the logged in user."""

import MySQLdb
import cgi


def preffered_update():
    """Updating the preffered communication medium."""
    form = cgi.FieldStorage()
    # connect to the database
    db = MySQLdb.connect("localhost", "user1", "mindfire", "assignment")
    # setup a cursor object using cursor() method
    cursor = db.cursor()

    user_detail_id = form.getvalue('user_detail_id')
    mail = form.getvalue('mail')
    message = form.getvalue('message')
    phone_call = form.getvalue('phone_call')
    other = form.getvalue('other')

    print "Content-type:text/html\r\n\r\n"
    print
    print '<html>'
    print '<head>'
    print '<title>Edit Page</title>'
    print '</head>'
    print '<body>'

    # updating the the personal information'
    try:
        sql_status = "UPDATE user_detail SET mail='{0}',message='{1}',phone_call='{2}',\
        other='{3}' WHERE user_detail_id = {4}".format(
            mail, message, phone_call, other, user_detail_id
        )
        cursor.execute(sql_status)
        db.commit()

        line = open('../static/html_data/editfile.text')
        try:
            sql_display = "SELECT first_name,last_name,date_of_birth,martial_status,\
            gender,address_line_1,address_line_2,street,zip,contact_number,extra_note,mail,message,\
            phone_call,other,image_path FROM user_detail \
            where user_detail_id='{0}'".format(user_detail_id)
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

            if martial_status == "single":
                single = "selected"
            else:
                single = " "
            if martial_status == "married":
                married = "selected"
            else:
                married = " "

            if gender == "male":
                male = "checked"
            else:
                male = " "
            if gender == "female":
                female = "checked"
            else:
                female = " "

            if mail == 1:
                mail = "checked"
            else:
                mail = " "
            if message == 1:
                message = "checked"
            else:
                message = " "
            if phone_call == 1:
                phone_call = "checked"
            else:
                phone_call = " "
            if other == 1:
                other = "checked"
            else:
                other = " "

            print ''.join(line).format(
                first_name, last_name, date_of_birth, single, married, male,
                female, address_line_1, address_line_2, street, zip_code,
                contact_number, extra_note, mail, message, phone_call, other,
                user_detail_id, image_path)

        except Exception as e:
            print
            print '<html>'
            print '<head>'
            print '<title>Edit</title>'
            print '</head>'
            print '<body>'
            print '<h1>Oops!</h1>'
            print "<p>{{0}</p>".format(e)  # error in fetching all the records

    except:
        print "<br>Error in Updation"
        db.rollback()

    print '</body>'
    print '</html>'

    # close the mysql database connection
    db.close()

preffered_update()
