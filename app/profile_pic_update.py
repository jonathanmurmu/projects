#!/usr/bin/python
"""Uploading the file to the directory and updates the database."""
import cgi
import os
import MySQLdb
import cgitb
import uuid
import msvcrt


def profile_pic_update():
    """Uploading the file to the directory."""
    cgitb.enable()
    # connect to database
    db = MySQLdb.connect("localhost", "user1", "mindfire", "assignment")
    # setup a cursor object
    cursor = db.cursor()

    try:  # Windows needs stdio set for binary mode.
        msvcrt.setmode(0, os.O_BINARY)  # stdin  = 0
        msvcrt.setmode(1, os.O_BINARY)  # stdout = 1
    except ImportError:
        pass

    form = cgi.FieldStorage()
    # A nested FieldStorage instance holds the file
    fileitem = form['profile_pic']
    user_detail_id = form.getvalue('user_detail_id')
    print "Content-type:text/html\r\n\r\n"
    print

    if fileitem.filename:

        # strip leading path from filename to avoid directory traversal attacks
        fn = os.path.basename(fileitem.filename)
        # writing the file to the server directory
        unique_name = uuid.uuid4().fields[0]
        open('../static/images/{0}{1}'.format(unique_name, fn), 'wb').write(
            fileitem.file.read()
        )
        message = 'The file {0} was uploaded successfully in server'.format(fn)
        path = "/cgi-bin/projects/task/static/images/{0}{1}".format(
            unique_name, fn
        )

        # storing the image path to database
        try:
            sql = "UPDATE user_detail SET image_path='{0}' \
            WHERE user_detail_id='{1}'".format(path, user_detail_id)
            cursor.execute(sql)
            db.commit()

            line = open('../static/html_data/editfile.text')
            try:
                sql_display = "SELECT first_name,last_name,date_of_birth,\
                martial_status,gender,address_line_1,address_line_2,street,zip,\
                contact_number,extra_note,mail,message,phone_call,other,\
                image_path FROM user_detail \
                WHERE user_detail_id='{0}'".format(user_detail_id)

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
                    first_name, last_name, date_of_birth, single, married,
                    male, female, address_line_1, address_line_2, street,
                    zip_code, contact_number, extra_note, mail, message,
                    phone_call, other, user_detail_id, image_path)

            except:
                # error in fetching records
                print
                print '<html>'
                print '<head>'
                print '<title>Edit</title>'
                print '</head>'
                print '<body>'
                print '<h1>Oops!</h1>'
                print "<h2>Conection problem !!!</h2>"

        except Exception as e:
            print "<p>{0}</p>".format(e)
            db.rollback()

    else:
        print "<p>Error uploading pic</p>"

    print '</body>'
    print '</html>'

    # close the mysql database connection
    db.close()

profile_pic_update()
