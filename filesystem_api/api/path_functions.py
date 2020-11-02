from pathlib import Path
from filesystem_api.filesys_functions.project_safety import project_dir_safe_path
import settings

@project_dir_safe_path
def path_to_apipath(*, path: Path) -> str:
    return str(path).replace(str(settings.API_ROOT_DIR), '')


def apipath_to_path(*, apipath: str) -> Path:
    return settings.API_ROOT_DIR / apipath