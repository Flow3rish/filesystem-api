import settings

class DirSafetyException(Exception):
    pass

def project_dir_safe_path(func):
    def wrapper(*args, **kwargs):
        if settings.API_ROOT_DIR in kwargs['path'].parents or settings.API_ROOT_DIR == kwargs['path']:
            return func(*args, **kwargs)
        else:
            raise DirSafetyException('Acessing outside project root.')
    return wrapper