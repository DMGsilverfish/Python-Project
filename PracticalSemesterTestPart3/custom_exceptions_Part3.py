# custom_exceptions.py

class FileImportError(OSError):
    def __init__(self, message):
        super().__init__(message)