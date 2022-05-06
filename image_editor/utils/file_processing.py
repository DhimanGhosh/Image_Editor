import os


def get_file_size(file_path: str) -> int:
    """
    get file size in bytes
    """
    file_size = os.path.getsize(file_path)
    return file_size
