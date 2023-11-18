from Files.file_base import FileBase

class TextFile(FileBase):
    def __init__(self):
        super().__init__(".txt")
    
    def insert(self, string_data):
        if not isinstance(string_data, str):
            raise ValueError("Wrong type")
        
        if self.info is None or not self.info.exists:
            return "Файл необходимо создать перед использованием!"
        
        with self.info.open('w') as stream:
            stream.write(string_data)
        
        return f"Строка \"{string_data}\" успешно вставлена в файл"