import sqlite3
connection = sqlite3.connect('ebay.db')
cursor = connection.cursor()
level = '1'
cursor.execute('SELECT * FROM categories where CategoryLevel=?', level)
categories = cursor.fetchall()

cursor.close()
connection.close()
