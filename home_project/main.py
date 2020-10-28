import geopandas as gpd
import pandas as pd

from settings import DATA_DIRECTORY, FILENAMES
from utils import check_if_float, round_data


def get_data(filename, directory=DATA_DIRECTORY):
    return clean_up_data(pd.read_csv(directory / filename))


def clean_up_data(df):
    df = df.rename(columns={"lat": "Latitude", "long": "Longitude"})
    return round_data(
        df[
            df["Latitude"].apply(
                check_if_float
            )  # Filter out any rows that don't have float Latitude values
        ]
    )


def validate_data(row):
    if row["Location"].split(",")[-1].strip() == row["postcode"]:
        return True
    return False


def main():
    data_frames = [get_data(filename) for filename in FILENAMES]
    geo_data = [
        gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
        for df in data_frames
    ]
    joined_data = gpd.sjoin(geo_data[0], geo_data[1], op="intersects")
    joined_data["validated"] = joined_data.apply(lambda row: validate_data(row), axis=1)
    pd.DataFrame(joined_data.drop(columns="geometry")).to_csv(
        "address_list.tsv", sep="|"
    )


if __name__ == "__main__":
    main()
