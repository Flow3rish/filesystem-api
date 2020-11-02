from filesystem_api.filesys_functions.project_safety import project_dir_safe_path
from pathlib import Path

@project_dir_safe_path
def touch(*, path: Path) -> Path:
    path.touch()
    return path

@project_dir_safe_path
def rm(*, path: Path) -> Path:
    path.unlink()
    return path

@project_dir_safe_path
def mkdir(*, path: Path) -> Path:
    path.mkdir()
    return path

@project_dir_safe_path
def rmdir(*, path: Path) -> Path:
    path.rmdir()
    return path

