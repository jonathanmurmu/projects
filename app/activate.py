#!/usr/bin/python
"""Sendig an activation link."""
import MySQLdb
import cgi
import cgitb


def activate():
    """Activate the user and send activation link via email."""
    form = cgi.FieldStorage()
    # connect to the database
    db = MySQLdb.connect("localhost", "user1", "mindfire", "assignment")
    cgitb.enable()
    # setup a cursor object using cursor() method
    cursor = db.cursor()
    user_id = form.getvalue('id')

    print "Content-type:text/html\r\n\r\n"
    print
    print '<html>'
    print '<head>'
    print '<title>Activation</title>'
    print '</head>'
    print '<body>'

    # updating the status from 'inactive' to 'active'
    try:
        sql_status = "UPDATE user_detail SET status='active' WHERE \
        user_detail_id = {0}".format(user_id)
        cursor.execute(sql_status)
        print '<h2>Your account is acctive.</h2>'
        print '<h3>Please <a href="http://localhost/cgi-bin/projects/task/static/\
        html/login.html">login</a> to continue<h3>'

        db.commit()
    except:
        print "<br>Error in activation"
        db.rollback()

    print '</body>'
    print '</html>'

    # close the mysql database connection
    db.close()

activate()
