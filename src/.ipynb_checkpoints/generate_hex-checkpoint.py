import geopandas as gpd
import pandas as pd
import shapely as sh
import h3

def tessellate_hex(boundry_gdb, res = 7):
    boundry_h3 = h3.geo_to_h3shape(boundry_gdb.iloc[0].__geo_interface__)
    hex_list = h3.h3shape_to_cells(boundry_h3, res)
    geos = []
    for hex_id in hex_list:
        h3_boundary = h3.cell_to_boundary(hex_id)
        h3_boundary_geojson = [(lng, lat) for lat, lng in h3_boundary]
        poly = sh.Polygon(h3_boundary_geojson)
        geos.append({
            'id':hex_id,
            'geometry': poly
        })
    df = pd.DataFrame(geos)
    df['id'] = df.index
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    return gdf

def tessellate_hex_id(boundry_gdb, res = 7):
    boundry_h3 = h3.geo_to_h3shape(boundry_gdb.iloc[0].__geo_interface__)
    hex_list = h3.h3shape_to_cells(boundry_h3, res)
    geos = []
    for hex_id in hex_list:
        h3_boundary = h3.cell_to_boundary(hex_id)
        h3_boundary_geojson = [(lng, lat) for lat, lng in h3_boundary]
        poly = sh.Polygon(h3_boundary_geojson)
        geos.append({
            'id':hex_id,
            'geometry': poly
        })
    df = pd.DataFrame(geos)
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    return gdf

if __name__ == '__main__':
    tor_boundry = gpd.read_file('tor_boundry.geojson')
    boundry_geo = tor_boundry.geometry
    tor_tess = tessellate_hex(boundry_geo)