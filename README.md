My Feed Installation
====================

1. Setup python virtualenv via `sudo pip install virutalenv`.
2. In a project directory, type virutanlenv env to create a python virtual environment.
3. (optional) install virtualenv_cd_alias via 
`git clone https://github.com/patrick-dowell/shell_stuff.git`
4. Install MySQL if you don't have it from <http://www.mysql.com/downloads/mysql/>.
5. Download MySQL-python from <http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.2/MySQL-python-1.2.2.tar.gz/download>.
6. Once inside your virtualenv, move MySQL-python to your virtualenv by typing `mv ~/Downloads/MySQL-python-1.2.2 ./`.
7. Run `tar xvfz MySQL-python-1.2.2.tar.gz`.
8. Run `cd MySQL-python-1.2.2`.
9. Run `vi setup_posix.py`.
10. Type `:s/"mysql_config"/"\/usr\/local\/mysql-5.5.25-osx10.6-x86_64\/bin\/mysql_config"/g` and hit enter to replace `"mysql_config"` with `"/usr/local/mysql-5.5.25-osx10.6-x86_64/bin/mysql_config"`. (Note that the path `/usr/local/mysql-5.5.25-osx10.6-x86_64/bin/mysql_config` should exist and be valid on your machine before performing this step.)
11. Type `:x` and hit enter to save and quit.
12. Edit `_mysql.c` lines 37, 38, and 39 as follows:

		//#ifndef uint
		//#define uint unsigned int
		//#endif
13. Run `sudo python setup.py build`.
14. Run `sudo python setup.py install`.
15. Return to your python virtual environment and install Django via `pip install django`.
16. Verify your installation by typing `python` and executing the following:

		>>>import MySQLdb
		>>>MySQLdb.apilevel
		'2.0'
		>>>import django
		>>>print django.VERSION
		(1, 4, 0, 'final', 0)
		>>>exit() 
		
17. Run `cd ..` to go back one directory.
18. Next, create a database called `myfeed` using Sequel Pro (<http://www.sequelpro.com/download/>). Make sure your mysql server is running at this point.
19. Now, run `git clone https://github.com/patrick-dowell/my-daily-feed.git`.
20. Config github via <https://help.github.com/articles/set-up-git>.
21. run `python manage.py syncdb` in my_daily_feed/mysite to sync the myfeed database.
22. run `python manage.py runserver` to start the server.