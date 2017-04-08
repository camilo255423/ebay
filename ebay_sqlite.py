import sqlite3
connection = sqlite3.connect('ebay.db')
cursor = connection.cursor()
cursor.execute("""DROP TABLE Categories""")
cursor.execute\
    ("""CREATE TABLE Categories (CategoryID INTEGER,CategoryName TEXT, CategoryLevel INTEGER, BestOfferEnabled TEXT, CategoryParentID INTEGER)""")
cursor.close()
connection.close()
