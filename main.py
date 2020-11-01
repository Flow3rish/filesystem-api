from src.filesys_functions.info_functions import list_all_with_info, list_detail_with_info
from src.api.path_functions import apipath_to_path, path_to_apipath
from src.constants import API_ROOT_DIR
from fastapi import FastAPI


app = FastAPI()
