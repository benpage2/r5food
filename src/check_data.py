from pyrosm import get_data
import os

def get_cwd():
    current_dir = os.getcwd()
    return current_dir

def is_dir(folder_name):
    if not os.path.isdir(folder_name):
        raise Exception(f"Folder {folder_name} not found in {current_dir}")
    return True

def is_file(file_dir):
    
        return True
    else:
        return False

def download_extract(location, data_dir):
    extract = get_data(location, directory=data_dir)
    print("Data was downloaded to:", extract)

def check_all(extract_dir, gtfs_dir):
    if os.path.isfile(extract_dir):
        Print('OSM extract found (1/3)')
    else:
        raise Exception(f'OSM Extract not found. Download data or check extract_dir in main')
    if os.path.isfile(gtfs_dir):
        Print('GTFS file found. Checking format')
        
    
if __name__=='__main__':
    study_area = 'Toronto'
    extract_dir = '/Users/benpage/Documents/GitHub/r5food/data/Toronto.osm.pbf'
    osm_extract_name = 'Toronto.osm.pbf'
    gtfs_name=
    