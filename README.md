# Download Aeronet Data (DAD)

Python tools to download AERONET Version 3 data from the
[AERONET Web Data Service](https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3).

Supported products include:

- Aerosol Optical Depth (direct sun), Level 1.5 or 2.0
- Inversion products (size distribution, refractive index, SSA, phase functions, and related fields)

## Requirements

- Python 3
- `pandas`
- `wget` (Python package)

Example with a virtual environment:

```bash
source ~/.venv/DL/bin/activate
pip install pandas wget
```

## Station names

Use exact AERONET site names (for example `Sao_Paulo`, `Lahore`, `GSFC`).
Valid names are listed in [`aeronet_locations_v3.csv`](aeronet_locations_v3.csv).

`dad_mod.py` checks the station name against that file before downloading.

## Workflows

There are two ways to download data.

### 1. CLI: single station (`dad_mod.py`)

Builds a per-station input CSV, then downloads all products that are marked `on`.
By default this uses Level 1.5 (`level=15`) and all points (`avg=10`).

```bash
python dad_mod.py \
  --station Lahore \
  --start_date 2024-08-01 \
  --end_date 2024-12-31 \
  --output_dir 01-rawdata/V4-GRASP-QuickCheck \
  --input_dir aeronet_list
```

| Argument | Description |
| --- | --- |
| `-n`, `--station` | AERONET site name |
| `-s`, `--start_date` | Start date (`YYYY-MM-DD`) |
| `-e`, `--end_date` | End date (`YYYY-MM-DD`) |
| `-o`, `--output_dir` | Directory for downloaded files |
| `-i`, `--input_dir` | Directory for generated input CSVs |

Generated input files are written as `input1_<station>.csv` under `--input_dir`.
Downloads run quietly (no wget progress bar); each saved file is reported on stdout.

### 2. Batch: several stations (`download_list.py`)

Edit the station list, date range, and directories in `download_list.py`, then run:

```bash
python download_list.py
```

That script loops over the configured stations and calls `dad_mod.py` for each one.

### 3. CSV batch (`dad.py`)

Reads input CSVs whose names start with `input1` from a fixed input directory
(currently `aeronet_list/`) and writes downloads to `01-rawdata/` by default.
Adjust paths near the top of `dad.py` if needed, then:

```bash
python dad.py
```

## Input CSV format

Input CSVs (under `01-input_dir/` or generated under `aeronet_list/`) have 11 columns:

1. `year_initial` - start year
2. `month_initial` - start month
3. `day_initial` - start day
4. `year_final` - end year
5. `month_final` - end month
6. `day_final` - end day
7. `site` - AERONET station name (see `aeronet_locations_v3.csv`)
8. `level` - data level: `15` for Level 1.5, `20` for Level 2.0
9. `avg` - averaging: `10` for all points, `20` for daily average
10. `products` - product code (see below)
11. `download` - `on` or `off`

Example (see also [`01-input_dir/input1.csv`](01-input_dir/input1.csv)):

```csv
year_initial,month_initial,day_initial,year_final,month_final,day_final,site,level,avg,products,download
2017,9,1,2021,8,31,Sao_Paulo,15,10,siz,on
2017,9,1,2021,8,31,Sao_Paulo,15,10,directsun,on
```

When using `dad_mod.py`, `funcLibrary.write_station_csv` creates this file with
default product flags (several products on, some off). Edit the generated CSV
or the defaults in `funcLibrary.py` to change which products are downloaded.

## Products

| Code | Description |
| --- | --- |
| `siz` | Size distribution |
| `rin` | Refractive indices (real and imaginary) |
| `cad` | Coincident AOT with almucantar retrieval |
| `vol` | Volume concentration, volume mean radius, effective radius, standard deviation |
| `tab` | AOD absorption |
| `aod` | AOD extinction |
| `ssa` | Single scattering albedo |
| `asy` | Asymmetry factor |
| `frc` | Radiative forcing |
| `lid` | Lidar and depolarization ratios |
| `flx` | Spectral flux |
| `pfn` | Phase function |
| `pfncoarse` | Coarse-mode phase functions |
| `pfnfine` | Fine-mode phase functions |
| `directsun` | Aerosol optical depth from direct sun measurements |

Output files are named:

```text
YYYYMMDD_YYYYMMDD_<site>_level<level>.<product>
```

for example `20240801_20241231_Lahore_level15.directsun`.

## Related scripts

| Script | Role |
| --- | --- |
| `dad_mod.py` | CLI download for one station |
| `download_list.py` | Batch driver over a station list |
| `dad.py` | Download from pre-made `input1*.csv` files |
| `funcLibrary.py` | Station validation and input CSV generation |
| `plot_aeronet_data.py` | Plotting helpers for downloaded data |

## Reference

More information on products and request parameters:

[AERONET Web Data Service Help](https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3)
