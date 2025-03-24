import geopandas as gpd
import shapely as sh
def create_boundry(neighbourhoods):
    city_boundry = 


def main():
    study_area = 'Toronto'
    gtfs_dir = '/Users/benpage/Documents/GitHub/r5food/data/ttc_gtfs.zip'
    osm_extract_dir = '/Users/benpage/Documents/GitHub/r5food/data/Toronto.osm.pbf'

    neighborhoods = gpd.read_file('neighborhoods.geojson')
    

if __name__ == '__main__':
    main()