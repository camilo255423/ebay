class HTMLTree:
    def __init__(self, db):
        self.db = db

    def get_html_tree(self, category_id):
        if not self.db.exist_category(category_id):
            raise Exception("Category doesn't exist")
        document = "\n"
        document += "<ul>"
        document += "<li>"
        document += str(category_id)
        document += "</li>"
        children = self.db.get_category_children(category_id)
        if children:
            for child in children:
                document += self.get_html_tree(child[0])

        document += "</ul>"
        return document

    def to_file(self, file='1.html', category_root_id=1):
        if not self.db.exist_category(category_root_id):
            raise Exception("Category doesn't exist")
        file_name = '{}.html'.format(category_root_id)
        with open(file_name, mode='w') as file:
            file.write(self.get_html_tree(category_id=category_root_id))


