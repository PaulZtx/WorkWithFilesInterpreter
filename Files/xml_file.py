from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree
from Files.file_base import FileBase
from Entities.student import Student

class XmlFile(FileBase):
    def __init__(self):
        super().__init__(".xml")
        
    def insert(self, data):
        if not isinstance(data, Student):
            raise ValueError("Wrong type")
        
        if self.info is None or not self.info.exists:
            return "Файл необходимо создать перед использованием!"
        
        root = Element("student")
        name = SubElement(root, "name")
        name.text = data.name
        group = SubElement(root, "group")
        group.text = data.group
        
        tree = ElementTree.ElementTree(root)
        tree.write(self.info, encoding="utf-8", xml_declaration=True)
        
        return "Файл успешно создан"