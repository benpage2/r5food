from src import get_cwd
from src import is_dir
from src import get_folder_dir
from src import download_extract
from src import is_file

def tests():
    print('Checking get_dir...')
    curent_dir = get_cwd()
    print('Current directory ' + curent_dir)
    
    print('Checking for data folder...')
    print(is_dir('data'))

    print('Getting data folder directory...')
    data_dir = get_folder_dir('data')
    print(data_dir)

    print('Downloading GTFS...')
    download_extract('Toronto', data_dir)
    
    print('Checking a file...')
    print(is_file(data_dir, 'Toronto.osm.pbf'))


if __name__ == '__main__':
    tests()
