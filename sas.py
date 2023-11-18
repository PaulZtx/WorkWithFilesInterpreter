from Files.text_file import TextFile
from Files.json_file import JsonFile
from Files.xml_file import XmlFile
from Archives.zip_archive import ZipArchive
from Entities.student import Student
#import os

file = ZipArchive()
print(file.create('sas228'))
print(file.add_file('test.txt'))
print(file.unzip())
print(file.delete())
