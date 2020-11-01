from src.constants import API_ROOT_DIR

class DirSafetyException(Exception):
    pass

def project_dir_safe_path(func):
    def wrapper(*args, **kwargs):
        if API_ROOT_DIR in kwargs['path'].parents or API_ROOT_DIR == kwargs['path']:
            return func(*args, **kwargs)
        else:
            raise DirSafetyException('Acessing outside project root.')
    return wrapper