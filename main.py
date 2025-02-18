from src import download_data

def main():
    location = 'Toronto'
    data_dir = '/Users/benpage/Documents/GitHub/r5food/data'
    download_data(location, data_dir)

if __name__ == '__main__':
    main()