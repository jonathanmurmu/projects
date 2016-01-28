Assginment - Login, signup and profile page.
==================================================
Packages required for executing the assgingment :-

1. MySQLdb
2. validate_email
3. cgi

Path required for executing the assginment in browser :- 
  http://localhost/cgi-bin/projects/task/static/html/login.html

CGI configuration :-
---------------------------------------------------
serve-cgi-bin.conf

		AddHandler cgi-script .cgi .py
		AllowOverride None
		Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		Require all granted

inside < Directory "/var/www/html/cgi-bin" > tag


Note :- Please keep the 'app' and 'static' folder inside '/var/www/cgi-bin/projects/task/' directory. And make sure that your Web Server supports CGI and it is configured to handle CGI Programs.
