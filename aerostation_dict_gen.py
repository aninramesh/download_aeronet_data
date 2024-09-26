import csv

data = '/Users/aputhukkudy/git/download_aeronet_data/HARP2_2024_aeronet_stations_sorted_lon.csv'

# Read the CSV data

stations = []
station_name = []

with open(data, 'r') as f:
    # read the csv file
    reader = csv.reader(f)
    # Skip the first row
    next(reader)
    next(reader)
    for row in reader:
        site_name = row[0]
        longitude = float(row[1])
        latitude = float(row[2])
        elevation = float(row[3])
        
        lower_left_lon = round(longitude - 0.05, 5)
        lower_left_lat = round(latitude - 0.05, 5)
        upper_right_lon = round(longitude + 0.05, 5)
        upper_right_lat = round(latitude + 0.05, 5)
        
        stations.append([(lower_left_lon, lower_left_lat, upper_right_lon, upper_right_lat), latitude, longitude])
        station_name.append(site_name)

# Example usage
for i, station in enumerate(stations):
    print(f"stations_['{station_name[i]}'] = {station}")

for i, station in enumerate(stations):
    print(f"'{station_name[i]}',")