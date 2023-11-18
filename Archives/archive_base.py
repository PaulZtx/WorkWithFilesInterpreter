import os
from pathlib import Path

class ArchiveBase:
    def __init__(self, format):
        self.dir = os.path.expanduser('~\\Documents')
        self.format = format
        self.fileInfo:Path = None
        self.info:Path = None

    def delete(self):
        if self.info is None or not self.info.exists:
            return "Архив необходимо создать перед удалением!"
        
        if self.fileInfo is None or not self.fileInfo.exists:
            return "Файл необходимо разархивировать перед удалением!"
        
        self.info.unlink()
        self.fileInfo.unlink()
        
        return "Архив и файл удалены успешно"