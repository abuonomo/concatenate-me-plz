# Concatenate Data

A script for concatenating data from multiple csv files in a given directory. The script will retain the headers and repeat them on every other row of the output contentated file. This is an oddity which is needed for downstream processing.

## Usage
You will need to place the directory with the csvs you want to concatenate into the `data` directory with the title `All_subjects_spreadsheets`.

While in the root of this repository, run the following command:
```bash
python src/merge.py
```
By default, this will use the input data directory located at `<project root>/data/All_subjects_spreadsheets` and will output the results to `<project_root>/data/concatenated.csv`.  

If, however, you want to customize these values, you may run:

```bash
python src/merge.py --indir <path to input directory> --outfile <path to output file>
```

## Installation

This project was developed and tested with Python 3.11.2. It uses the `pandas` and `tqdm` packages.  
To install dependencies into your local environment, run the following command:

```bash
pip install -r requirements.txt
```

