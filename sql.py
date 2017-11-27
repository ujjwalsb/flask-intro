import sqlite3

with sqlite3.connect ('sample.db') as connection:
	c = connection.cursor()

	c.execute('create table posts(title TEXT, details TEXT)')
	c.execute('insert into posts values("Good", "I am good.")')
	c.execute('insert into posts values("well", "I am well")')
	c.execute('insert into posts values("Excellent", "I am Excellent")')
	c.execute('insert into posts values("Okay", "I am Okay")')