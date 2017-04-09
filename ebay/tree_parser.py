from ebay.persistence import NoCategoryException
class HTMLTree:
    def __init__(self, db):
        self.db = db

    def get_html_tree(self, category, root_node=False):
        if not self.db.exist_category(category[0]):
            raise Exception("Category doesn't exist")
        document = "\n"
        if root_node:
            document += "<ul id = 'treeview' class = 'treeview-black'><li>"
        else:
            document += "<ul><li>"
        children = self.db.get_category_children(category[0])
        if children:
            document += "<span>"+self.get_html_node(category)+"</span>"
            for child in children:
                document += self.get_html_tree(child)
        else:
            document += self.get_html_node(category)
            document += "<ul></ul>"
        document += "</li></ul>"
        return document

    def get_html_node(self, category):
        document = ""
        document += "<span class='categoryId'>ID: "+str(category[0])+"</span>"
        document += "<span class='categoryName'> Name: " + str(category[1])+"</span>"
        document += "<span class='categoryLevel'> Level: " + str(category[2])+"</span>"
        document += "<span class='categoryBestOffer'> BestOfferEnabled: " + str(category[3])+"</span>"
        return document

    def load_template(self, file_name):
        string = ""
        with open(file_name) as file:
            for line in file.readlines():
                string += line
        return string

    def to_file(self, file='1.html', category_root_id=1, template_file="templates/template.html"):
        if not self.db.exist_category(category_root_id):
            raise NoCategoryException("Category doesn't exist")
        file_name = '{}.html'.format(category_root_id)
        template_str = self.load_template(template_file)
        with open(file_name, mode='w') as file:
            category = self.db.get_category_by_id(category_root_id)
            str_tree = self.get_html_tree(category=category, root_node=True)
            html_tree = template_str.replace("{content}", str_tree)
            file.write(html_tree)


