from Drives.drives_info import DrivesInfo
from Files.text_file import TextFile
from Files.json_file import JsonFile
from Files.xml_file import XmlFile
from Archives.zip_archive import ZipArchive
from Entities.student import Student
import os

fileTxt = TextFile()
fileJson = JsonFile()
fileXml = XmlFile()
archive = ZipArchive()

def choose_action():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| File Utils |")
    print("--------------")
    print("0 - Drives Info")
    print("1 - Text")
    print("2 - Json")
    print("3 - Xml")
    print("4 - Zip")
    key = input("Enter your choice: ")
    
    if key == '1':
        print_text_menu()
    elif key == '2':
        print_json_menu()
    elif key == '3':
        print_xml_menu()
    elif key == '4':
        print_zip_menu()
    elif key == '0':
        print_drives_info()
    else:
        print("Wrong key!")

def print_drives_info():
    os.system('cls' if os.name == 'nt' else 'clear')
    DrivesInfo.print()

def print_text_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| File Utils / Text |")
    print("---------------------")
    print("1 - Create file")
    print("2 - Insert string into file")
    print("3 - Read file")
    print("4 - Delete file")
    key = input("Enter your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if key == '1':
        print(fileTxt.create(input("File name: ")))
    elif key == '2':
        print(fileTxt.insert(input("String: ")))
    elif key == '3':
        print(fileTxt.read())
    elif key == '4':
        print(fileTxt.delete())
    else:
        print("Wrong key!")

def print_json_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| File Utils / Json |")
    print("---------------------")
    print("1 - Create file")
    print("2 - Insert Student into file")
    print("3 - Read file")
    print("4 - Delete file")
    key = input("Enter your choice: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if key == '1':
        print(fileJson.create(input("File name: ")))
    elif key == '2':
        name = input("Student name: ")
        group = input("Student group: ")
        student = Student(name, group)
        print(fileJson.insert(student))
    elif key == '3':
        print(fileJson.read())
    elif key == '4':
        print(fileJson.delete())
    else:
        print("Wrong key!")

def print_xml_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| File Utils / Xml |")
    print("--------------------")
    print("1 - Create file")
    print("2 - Insert Student into file")
    print("3 - Read file")
    print("4 - Delete file")
    key = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if key == '1':
        print(fileXml.create(input("File name: ")))
    elif key == '2':
        print(fileXml.insert(Student(input("Student name: "), input("Student group: "))))
    elif key == '3':
        print(fileXml.read())
    elif key == '4':
        print(fileXml.delete())
    else:
        print("Wrong key!")

def print_zip_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("| File Utils / Zip |")
    print("--------------------")
    print("1 - Create archive")
    print("2 - Insert file into archive")
    print("3 - Extract file from archive")
    print("4 - Delete archive and file")
    key = input()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if key == '1':
        print(archive.create(input("Archive name: ")))
    elif key == '2':
        print(archive.add_file(input("File name: ")))
    elif key == '3':
        print(archive.unzip())
    elif key == '4':
        print(archive.delete())
    else:
        print("Wrong key!")

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    choose_action()
    input("Press any key to continue...")