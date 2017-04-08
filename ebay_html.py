import sqlite3
connection = sqlite3.connect('ebay.db')
cursor = connection.cursor()


def get_html_tree(id_category):
    document = "\n"
    document += "<ul>"
    document += "<li>"
    document += str(id_category)
    document += "</li>"
    children = get_children(id_category)
    if children:
        for child in children:
            document += get_html_tree(child[0])

    document += "</ul>"
    return document


def get_children(id_category):
    cursor.execute('SELECT * FROM categories where CategoryParentID=? and CategoryID!=?', (id_category, id_category))
    children = cursor.fetchall()
    return children


file_name = '{}.html'.format(id)
with open(file_name,mode='w') as file:
    file.write(get_html_tree(id))

cursor.close()
connection.close()
