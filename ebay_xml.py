# {urn:ebay:apis:eBLBaseComponents}BestOfferEnabled
# {urn:ebay:apis:eBLBaseComponents}AutoPayEnabled
# {urn:ebay:apis:eBLBaseComponents}CategoryID
# {urn:ebay:apis:eBLBaseComponents}CategoryLevel
# {urn:ebay:apis:eBLBaseComponents}CategoryName
# {urn:ebay:apis:eBLBaseComponents}CategoryParentID
import sqlite3
import xml.etree.ElementTree as ET
tree = ET.parse('filename.xml')
root = tree.getroot()
categories = root[5]
connection = sqlite3.connect('ebay.db')
cursor = connection.cursor()
for category in categories:
    category_id =  category.find("{urn:ebay:apis:eBLBaseComponents}CategoryID").text \
        if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryID") is not None else None
    category_name = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryName").text \
        if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryName") is not None else None
    category_level = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryLevel").text \
        if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryLevel") is not None else None
    category_best_offer_enabled = category.find("{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled").text \
        if category.find("{urn:ebay:apis:eBLBaseComponents}BestOfferEnabled") is not None else None
    category_parent_id = category.find("{urn:ebay:apis:eBLBaseComponents}CategoryParentID").text\
        if category.find("{urn:ebay:apis:eBLBaseComponents}CategoryParentID") is not None else None

    sql = 'Insert into categories values (?,?,?,?,?)'
    values = (category_id, category_name, category_level, category_best_offer_enabled, category_parent_id)
    connection.commit()
    cursor.execute(sql, values)

cursor.close()
connection.close()