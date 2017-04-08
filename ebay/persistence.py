import sqlite3
import os.path
import xml.etree.ElementTree as ET

SQL_CREATE_TABLE = """CREATE TABLE Categories(
CategoryID INTEGER,
CategoryName TEXT,
CategoryLevel INTEGER,
BestOfferEnabled TEXT,
CategoryParentID INTEGER)"""


class CategoriesDB:
    def __init__(self, file_name='ebay.db', create=True):
        if create:
            try:
                os.remove(file_name)
            except OSError:
                pass
            finally:
                self.connection = sqlite3.connect(file_name)
                cursor = self.connection.cursor()
                cursor.execute(SQL_CREATE_TABLE)
        else:
            if not os.path.isfile(file_name):
                raise Exception("Data base doesn't exist")
            else:
                self.connection = sqlite3.connect(file_name)

    def populate_categories_from_xml(self, xml_string=None):
        tree = ET.fromstring(xml_string)
        categories = tree[5]
        cursor = self.connection.cursor()
        for category in categories:
            category_id = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryID").text \
                if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryID") is not None else None
            category_name = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryName").text \
                if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryName") is not None else None
            category_level = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryLevel").text \
                if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryLevel") is not None else None
            category_best_offer_enabled = category.find("{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled").text \
                if category.find("{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled") is not None else None
            category_parent_id = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryParentID").text \
                if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryParentID") is not None else None

            sql = 'Insert into categories values (?,?,?,?,?)'
            values = (category_id, category_name, category_level, category_best_offer_enabled, category_parent_id)

            self.connection.commit()
            cursor.execute(sql, values)

        cursor.close()
    
    def get_category_children(self, category_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM categories where CategoryParentID=? and CategoryID!=?', (category_id, category_id))
        children = cursor.fetchall()
        return children
    
    def exist_category(self, category_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM categories where CategoryID=?', (category_id,))
        return len(cursor.fetchall()) > 0 
    
    def close(self):
        self.connection.close()
