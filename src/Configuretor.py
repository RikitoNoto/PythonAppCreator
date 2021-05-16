from distutils import dir_util
import os

TEMPLATES_PATH = os.path.join("..","templates")

def create_configuration(path="."):
    if(not os.path.exists(path)):
        os.mkdir(path)
    __copy_templates(path)

def __copy_templates(path=".", source=TEMPLATES_PATH):
    dir_util.copy_tree(source, path)