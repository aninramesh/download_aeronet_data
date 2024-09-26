aeronet_stations = [
    {"station": "Banizoumbou", "longitude": 2.665190, "latitude": 13.546930, "elevation": 274},
    {"station": "Mongu", "longitude": 23.150833, "latitude": -15.253611, "elevation": 1047},
    {"station": "Kanpur", "longitude": 80.231639, "latitude": 26.512778, "elevation": 123},
    {"station": "Beijing", "longitude": 116.381370, "latitude": 39.976890, "elevation": 92},
    {"station": "Ilorin", "longitude": 4.674500, "latitude": 8.484100, "elevation": 400},
    {"station": "Solar_Village", "longitude": 46.397286, "latitude": 24.906933, "elevation": 764},
    {"station": "Alta_Floresta", "longitude": -56.104453, "latitude": -9.871339, "elevation": 277},
    {"station": "Ji_Parana_SE", "longitude": -61.85152, "latitude": -10.93425, "elevation": 218},
    {"station": "Cuiaba", "longitude": -56.070214, "latitude": -15.555244, "elevation": 234},
    {"station": "Mexico_City", "longitude": -99.181667, "latitude": 19.333611, "elevation": 2268},
    {"station": "CART_SITE", "longitude": -97.48639, "latitude": 36.60667, "elevation": 318},
    {"station": "GSFC", "longitude": -76.839833, "latitude": 38.992500, "elevation": 87},
    {"station": "Lille", "longitude": 3.141667, "latitude": 50.611667, "elevation": 60},
    {"station": "Ispra", "longitude": 8.626700, "latitude": 45.803050, "elevation": 235},
    {"station": "Thessaloniki", "longitude": 22.960000, "latitude": 40.630000, "elevation": 60},
    {"station": "Moldova", "longitude": 28.815600, "latitude": 47.000800, "elevation": 205},
    {"station": "Tomsk", "longitude": 85.048060, "latitude": 56.475351, "elevation": 174},
    {"station": "Lake_Argyle", "longitude": 128.748500, "latitude": -16.108100, "elevation": 150},
    {"station": "Paris", "longitude": 2.355508, "latitude": 48.846797, "elevation": 50},
    {"station": "Chiang_Mai", "longitude": 98.986944, "latitude": 18.813333, "elevation": 324},
    {"station": "Cabauw", "longitude": 4.927000, "latitude": 51.971000, "elevation": -0.7},
    {"station": "Granada", "longitude": -3.605000, "latitude": 37.164000, "elevation": 680},
    {"station": "SANTA_CRUZ_UTEPSA", "longitude": -63.200961, "latitude": -17.767325, "elevation": 432},
    {"station": "Ames", "longitude": -93.774778, "latitude": 42.021361, "elevation": 338},
    {"station": "Saada", "longitude": -8.155830, "latitude": 31.625830, "elevation": 420},
    {"station": "Belsk", "longitude": 20.791667, "latitude": 51.836667, "elevation": 190},
    {"station": "Kyiv", "longitude": 30.496667, "latitude": 50.363611, "elevation": 200},
    {"station": "UCSB", "longitude": -119.845360, "latitude": 34.415428, "elevation": 33},
    {"station": "Dushanbe", "longitude": 68.857911, "latitude": 38.553264, "elevation": 821},
    {"station": "Karlsruhe", "longitude": 8.427900, "latitude": 49.093300, "elevation": 140}
]

# Example usage
with open('grosat_aeronet_stations.csv', 'a') as f:
    for station in aeronet_stations:
        # print a csv of the list
        print(f"{station['station']},{station['longitude']},{station['latitude']},{station['elevation']}")
        # save the list to a csv for all stations
        f.write(f"{station['station']},{station['longitude']},{station['latitude']},{station['elevation']}\n")