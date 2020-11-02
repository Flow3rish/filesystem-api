from filesystem_api.filesys_functions.project_safety import project_dir_safe_path
from pathlib import Path


@project_dir_safe_path
def list_all_with_info(*, path: Path) -> list:
    return [x.name for x in path.glob('*')]

@project_dir_safe_path
def list_detail_with_info(*, path: Path) -> dict:
    """
    return detail info with system absolute path
    """
    return {
        'name': path.name,
        'size': path.stat().st_size,
        'time created': path.stat().st_ctime,
        'last modified': path.stat().st_mtime,
        'type': 'dir' if path.is_dir() else 'file'
    }