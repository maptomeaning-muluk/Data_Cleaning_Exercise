import pandas as pd
import geopandas as gpd
import os

# Path to the input CSV file
input_csv_path = r"D:\SpatialHawk\Kaggle\sn7_train_ground_truth_pix.csv\sn7_train_ground_truth_pix.csv"
output_directory = r"D:\SpatialHawk\Kaggle\Multiple_csvs_2"  # Specify your desired output directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Read the CSV file
df = pd.read_csv(input_csv_path)

# Convert the 'geometry' column from WKT format to GeoSeries
df['geometry'] = gpd.GeoSeries.from_wkt(df['geometry'])

# Group by the 'filename' attribute
grouped = df.groupby('filename')

# Save each group to a separate CSV file
for filename, group in grouped:
    # Create a GeoDataFrame from the group
    gdf = gpd.GeoDataFrame(group, geometry='geometry')

    # Define the output path
    output_path = os.path.join(output_directory, f'{filename}.csv')

    # Save the GeoDataFrame to a CSV file
    gdf.to_csv(output_path, index=False)

    print(f'Saved {output_path}')
