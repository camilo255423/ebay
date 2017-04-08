#!/usr/bin/env python3
import sys
from ebay.persistence import CategoriesDB
from ebay.request import get_xml_categories
from ebay.tree_parser import HTMLTree
parameter_error = True

if len(sys.argv) > 1:
    if sys.argv[1] == '--rebuild':
        xml_string = get_xml_categories()
        db = CategoriesDB(file_name='ebay3.db', create=True)
        db.populate_categories_from_xml(xml_string=xml_string)
        db.close()
        parameter_error = False

    if sys.argv[1] == '--render' and len(sys.argv) == 3:
        category_id = int(sys.argv[2])
        db = CategoriesDB(file_name='ebay3.db', create=False)
        file_name = str(category_id) + '.html'
        html_tree = HTMLTree(db)
        html_tree.to_file(file_name, category_id)
        db.close()
        parameter_error = False



if(parameter_error):
    print("Possible options:")
    print("./categories.py --rebuild")
    print("./categories.py --render categorieID")


