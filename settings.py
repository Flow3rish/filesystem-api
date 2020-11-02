from pathlib import Path

MODE = 'TEST'

API_ROOT_DIR = Path('./resources/api-root') if MODE == 'PROD' else Path('./test/resources/api-root')