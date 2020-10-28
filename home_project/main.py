import geopandas as gpd
import pandas as pd

from settings import DATA_DIRECTORY
from utils import check_if_float, round_data


def get_address_data():
    df = pd.read_csv(DATA_DIRECTORY / 'address_list.csv')
    return round_data(
        df[df['Latitude'].apply(check_if_float)])  # Filter out any rows that don't have float Latitude values


def get_post_code_data():
    df = pd.read_csv(DATA_DIRECTORY / 'postcode_reference.csv')
    return round_data(df.rename(columns={'lat': 'Latitude', 'long': 'Longitude'}))


def validate_data(row):
    if row['Location'].split(',')[-1].strip() == row['postcode']:
        return True
    return False


def main():
    addresses = get_address_data()
    post_codes = get_post_code_data()
    geo_addresses = gpd.GeoDataFrame(addresses, geometry=gpd.points_from_xy(addresses.Longitude, addresses.Latitude))
    geo_postcodes = gpd.GeoDataFrame(post_codes, geometry=gpd.points_from_xy(post_codes.Longitude, post_codes.Latitude))
    joined_data = gpd.sjoin(geo_addresses, geo_postcodes, op='intersects')
    joined_data['validated'] = joined_data.apply(lambda row: validate_data(row), axis=1)
    print(joined_data)
    print(len(joined_data))
    pd.DataFrame(joined_data.drop(columns='geometry')).to_csv('address_list.tsv', sep='|')


if __name__ == '__main__':
    main()
