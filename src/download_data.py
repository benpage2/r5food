from pyrosm import get_data
import os

def get_cwd():
    current_dir = os.getcwd()
    return current_dir

def is_dir(folder_name):
    current_dir = get_cwd()
    if not os.path.isdir(folder_name):
        raise Exception(f"Folder {folder_name} not found in {current_dir}")
    return True

def get_folder_dir(folder_name):
    current_dir = get_cwd()
    if is_dir(folder_name):
        return os.path.join(current_dir, folder_name)
    raise Exception(f"Folder {folder_name} not found in {current_dir}")

def download_extract(location, data_dir):
    extract = get_data(location, directory=data_dir)
    print("Data was downloaded to:", extract)

def is_file(data_dir, file_name):
    file_path = os.path.join(data_dir, file_name)
    
    if not os.path.isfile(file_path):
        raise Exception(f"The file: {file_name} was not found in: {data_dir}")
    return True