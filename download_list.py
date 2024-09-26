import os

# The list of stations to download data from the AERONET web data service
# stations_ = ['Amazon_ATTO_Tower',
#              'Rio_Branco',
#              'CUIABA-MIRANDA',
#              'Mongu_Inn',
#              'Sakeji_School',
#              'Gandhi_College',
#              'Kanpur',
#              'IITM_ARTCI_Bhopal',
#              'MCO-Hanimaadhoo',
#              'AAU_Jackros_ET',
#              'Tudor_Hill',
#              'ATTO-Campina',
#              'Selegua_BSRN',
#              'Toulouse_MF',
#              'Missoula',
#              'Stony_Plain', 
#              'St_Helena',
#              'Ascension_Island',]

stations_ = ['Lake_Argyle',
            'Beijing',
            'Chiang_Mai',
            'Tomsk',
            'Gandhi_College',
            'Kanpur',
            'Kanpur',
            'IITM_ARTCI_Bhopal',
            'MCO-Hanimaadhoo',
            'Dushanbe',
            'Solar_Village',
            'AAU_Jackros_ET',
            'Kyiv',
            'Moldova',
            'Sakeji_School',
            'Mongu',
            'Mongu_Inn',
            'Thessaloniki',
            'Belsk',
            'Ispra',
            'Karlsruhe',
            'Cabauw',
            'Ilorin',
            'Lille',
            'Banizoumbou',
            'Paris',
            'Toulouse_MF',
            'Granada',
            'St_Helena',
            'Saada',
            'Ascension_Island',
            'Cuiaba',
            'CUIABA-MIRANDA',
            'Alta_Floresta',
            'Amazon_ATTO_Tower',
            'ATTO-Campina',
            'Ji_Parana_SE',
            'SANTA_CRUZ_UTEPSA',
            'Tudor_Hill',
            'Rio_Branco',
            'GSFC',
            'Selegua_BSRN',
            'Ames',
            'CART_SITE',
            'Mexico_City',
            'Missoula',
            'Stony_Plain',
            'UCSB'
            ]

# start and end dates for the data download
start_date = '2024-03-05'
end_date = '2024-09-25'

# output directory for the downloaded data (use a clean/empty directory to avoid conflicts)
output_dir = '2024_v2'

# input directory for the input data (use a clean/empty directory to avoid conflicts)
input_dir = 'aeronet_data_HARP2_v2'

# loop over the stations to download the data
for station in stations_:
    print('--'*20)
    print('Downloading data for station:', station)
    # download the data
    os.system('python dad_mod.py --station %s \
              --start_date %s \
              --end_date %s \
              --output_dir %s \
              --input_dir %s' % (station, start_date, end_date, output_dir, input_dir))
    print('--'*20)
