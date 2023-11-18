from Files.file_base import FileBase
from Entities.student import Student
import json

class JsonFile(FileBase):
    def __init__(self):
        super().__init__(".json")
    
    def insert(self, data):
        if not isinstance(data, Student):
            raise ValueError("Wrong type")
        
        if self.info is None or not self.info.exists():
            return "Файл необходимо создать перед использованием!"
        
        with self.info.open('w') as fs:
            json.dump(data.__dict__, fs)
        
        return "Файл успешно изменен"