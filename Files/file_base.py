import os
from pathlib import Path

class FileBase:
    def __init__(self, format):
        self.dir = os.path.expanduser('~\\Documents')
        self.format = format
        self.info = None

    def create(self, filename):
        path = os.path.join(self.dir, filename + self.format)
        self.info = Path(path)
        with self.info.open('w'):
            pass

        return f"Файл {filename + self.format} создан успешно"

    def delete(self):
        if self.info is None or not self.info.exists():
            return "Файл необходимо создать перед использованием!"

        self.info.unlink()
        return "Файл удален успешно"

    def read(self):
        if self.info is None or not self.info.exists():
            return "Файл необходимо создать перед использованием!"

        with self.info.open('r') as stream:
            text_from_file = stream.read()

        return f"Текст из файла: {text_from_file}"