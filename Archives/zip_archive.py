from pathlib import Path
import zipfile
import os
from Archives.archive_base import ArchiveBase

class ZipArchive(ArchiveBase):
    def __init__(self):
        super().__init__(".zip")
    
    def create(self, archiveName):
        self.info = Path(os.path.join(self.dir, archiveName + self.format))
        with zipfile.ZipFile(self.info, 'w'):
            pass
        
        return f"Архив {archiveName + self.format} создан успешно"
    
    def add_file(self, fileName):
        if self.info is None or not self.info.exists:
            return "Архив необходимо создать перед использованием"
        
        fileInfo = Path(os.path.join(self.dir, fileName))
        if fileInfo.exists:
            self.fileInfo = fileInfo
        else:
            return f"Файл с именем {fileName} не найден"
        
        with zipfile.ZipFile(self.info, 'a') as zip:
            zip.write(self.fileInfo, self.fileInfo.name)
        
        self.fileInfo.unlink()
        return f"Файл {self.fileInfo} добавлен успешно"
    
    def unzip(self):
        if self.info is None or not self.info.exists:
            return "Архив необходимо создать перед использованием"
        
        with zipfile.ZipFile(self.info, 'r') as zip:
            zip.extractall(self.dir)
        
        return f"Файл {self.fileInfo.name} был успешно разархивирован"