from pathlib import Path
from src.filesys_functions.project_safety import project_dir_safe_path
from src.constants import API_ROOT_DIR


@project_dir_safe_path
def path_to_apipath(*, path: Path) -> str:
    return str(path).replace(str(API_ROOT_DIR), '')


def apipath_to_path(*, apipath: str) -> Path:
    return API_ROOT_DIR / apipath