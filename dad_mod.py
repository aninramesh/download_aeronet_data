"""
Created on Mon Feb  1 13:54:12 2021
@author: Fábio J. S. Lopes

Modified by:
@author: Anin Puthukkudy
Assistant Research Scientist
Earth and Space Institute, UMBC

Download Aeronet Data - DAD

Python script to automatically download data from AERONET Web Data Service Help platform. 
Dataset includes AERONET Aerosol Optical Depth - Version 3 - level1.5 or level2.0 data 
(direct sun algorithm) and AERONET inversion data

More information: Check AERONET Version 3 Web Service Help
https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3

"""

# ----------------------------------------------------------
# Importing libraries
# ----------------------------------------------------------

import os
import ssl
import wget
import platform
import pandas as pd
import argparse
import funcLibrary as fl
# ----------------------------------------------------------
# Enabling SSL certificate verification
# ----------------------------------------------------------

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
	ssl._create_default_https_context = ssl._create_unverified_context

# ----------------------------------------------------------
# Defining the input arguments
# ----------------------------------------------------------

parser = argparse.ArgumentParser(
	description='Download AERONET data from web data service')
parser.add_argument('-n', '--station', type=str,
					help='Input station name (e.g., Sao_Paulo), required=True')
parser.add_argument('-s', '--start_date', type=str,
					help='Input start date (e.g., 2017-09-01), required=True')
parser.add_argument('-e', '--end_date', type=str,
					help='Input end date (e.g., 2021-08-31), required=True')
parser.add_argument('-o', '--output_dir', type=str,
					help='Output directory for the downloaded data, required=True')
parser.add_argument('-i', '--input_dir', type=str,
					help='Input directory for the input data, required=True')
parser.add_argument('-v', '--version', action='version',
					version='%(prog)s 1.0')


args = parser.parse_args()

station_name = args.station
start_date = args.start_date
end_date = args.end_date
output_dir = args.output_dir

# -- print the run details
print('Station name:', station_name)
print('Start date:', start_date)
print('End date:', end_date)

# check if the output directory exists
if not os.path.exists(output_dir):
	os.makedirs(output_dir,exist_ok=True)

input_dir = args.input_dir
if not os.path.exists(input_dir):
	os.makedirs(input_dir,exist_ok=True)
input_file_name = 'input1_%s.csv' % station_name

# -- parse the start and end dates
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

station_file_name = os.path.join(input_dir, input_file_name)
# -- check if the station exists in the CSV file
fl.write_station_csv(station_name, start_date, end_date, station_file_name)

# ----------------------------------------------------------
# Main code
# ----------------------------------------------------------

'''Creating the folder for raw data download from AERONET web data service'''
rootdir = os.getcwd()
outputdir = output_dir
dircontents = os.sep.join([rootdir, outputdir])
if not os.path.exists(dircontents):
	os.makedirs(dircontents)

'''Reading the input data to download AERONET data from web data service'''
inputdatadir = input_dir
inputfilename = input_file_name
inputdir = os.sep.join([rootdir, inputdatadir])
filenames = [name for name in os.listdir(inputdir) if name.startswith(inputfilename)]
nfiles = len(filenames)

print(filenames)
filenameout = []

# ----------------------------------------------------------
# Downloading data from AERONET web data service
# ----------------------------------------------------------

for x in range(0, len(filenames)):
	newfile = os.sep.join([inputdir, filenames[x]])

	if platform.system() == 'Linux':
		filedata = pd.read_csv(newfile)
	else:
		filedata = pd.read_csv(newfile, sep=',')

	for i in range(0, len(filedata)):
		if filedata['download'][i] == 'on':
			if filedata['month_initial'][i] < 10:
				filemonthin = '0' + str(filedata['month_initial'][i])
			else:
				filemonthin = str(filedata['month_initial'][i])
			if filedata['month_final'][i] < 10:
				filemonthfinal = '0' + str(filedata['month_final'][i])
			else:
				filemonthfinal = str(filedata['month_final'][i])
			if filedata['day_initial'][i] < 10:
				filedayin = '0' + str(filedata['day_initial'][i])
			else:
				filedayin = str(filedata['day_initial'][i])
			if filedata['day_final'][i] < 10:
				filedayfinal = '0' + str(filedata['day_final'][i])
			else:
				filedayfinal = str(filedata['day_final'][i])
			if filedata['level'][i] == 10:
				filelevel = '10'
			elif filedata['level'][i] == 15:
				filelevel = '15'
			else:
				filelevel = '20'
			filenameout = str(filedata['year_initial'][i])+filemonthin+filedayin+'_' +\
				str(filedata['year_final'][i])+filemonthfinal+filedayfinal+'_' +\
				filedata['site'][i]+'_level' + \
				filelevel+'.'+filedata['products'][i]

			url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i] +\
				'&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin +\
				'&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal +\
				'&product='+filedata['products'][i].upper()+'&AVG='+str(
				filedata['avg'][i])+'&ALM'+filelevel+'=1&if_no_html=1'

			if filedata['products'][i] == 'pfncoarse':
				url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i] +\
				'&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin +\
				'&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal +\
				'&product=PFN&AVG=' + \
				str(filedata['avg'][i])+'&ALM' + \
				filelevel+'=1&if_no_html=1&pfn_type=1'

			if filedata['products'][i] == 'pfnfine':
				url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_inv_v3?site='+filedata['site'][i] +\
				'&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin +\
				'&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal +\
				'&product=PFN&AVG=' + \
				str(filedata['avg'][i])+'&ALM' + \
				filelevel+'=1&if_no_html=1&pfn_type=2'

			if filedata['products'][i] == 'directsun':
				url = 'https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3?site='+filedata['site'][i] +\
				'&year='+str(filedata['year_initial'][i])+'&month='+filemonthin+'&day='+filedayin +\
				'&year2='+str(filedata['year_final'][i])+'&month2='+filemonthfinal+'&day2='+filedayfinal +\
				'&AOD'+filelevel+'=1&AVG='+str(filedata['avg'][i])
			print('Downloading: ' + filenameout)
			filename = wget.download(
				url, out=os.sep.join([dircontents, filenameout]))