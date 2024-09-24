import csv
from datetime import datetime

def station_exists(station_name, csv_file='aeronet_locations_v3.csv'):
    '''
    Check if the given station name exists in the CSV file.

    Parameters:

        station_name (str): The name of the station.
        csv_file (str): The CSV file containing the station names.

    Returns:
        bool: True if the station name exists in the CSV file, False otherwise.

    Usage:
        # Check if the station name exists in the CSV file
        station_name = "Sao_Paulo"
        station_exists(station_name)
    '''

    assert station_name, "Station name cannot be empty."
    assert csv_file, "CSV file cannot be empty."

    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        next(reader)  # Skip the second row (metadata)
        
        for row in reader:
            if row[0] == station_name:
                return True
    return False

def write_station_csv(station_name, start_date, end_date, output_file, products=None):
    '''
    Write a CSV file with the given station name, start date, and end date.
    The CSV file will contain a list of products and their download status.

    Parameters:
        station_name (str): The name of the station.
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        output_file (str): The name of the output CSV file.
        products (list): A list of tuples containing the product name and download status.

    Returns:
        None

    Usage:
        # Define the station name, start date, and end date
        station_name = "Sao_Paulo"
        start_date = datetime(2017, 9, 1)
        end_date = datetime(2021, 8, 31)
        write_station_csv(station_name, start_date, end_date)
    '''

    assert station_exists(station_name), f"Station '{station_name}' does not exist in the CSV file."

    # List of products and their download status
    if products is None:
        products = [
            ("siz", "on"),
            ("rin", "on"),
            ("cad", "on"),
            ("vol", "off"),
            ("tab", "on"),
            ("aod", "on"),
            ("ssa", "on"),
            ("asy", "off"),
            ("frc", "off"),
            ("lid", "on"),
            ("flx", "off"),
            ("pfn", "on"),
            ("pfncoarse", "on"),
            ("pfnfine", "on"),
            ("directsun", "on")
        ]
    else:
        assert isinstance(products, list), "Products must be a list of tuples."

    # Open a new CSV file for writing
    print(f"Writing data to '{output_file}'")
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["year_initial", "month_initial", "day_initial", "year_final", "month_final", "day_final", "site", "level", "avg", "products", "download"])
        
        # Write the data rows
        for product, download in products:
            writer.writerow([
                start_date.year, start_date.month, start_date.day,
                end_date.year, end_date.month, end_date.day,
                station_name, 15, 10, product, download
            ])