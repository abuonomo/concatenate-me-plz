import argparse
import logging
from pathlib import Path

import pandas as pd
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)

DATA_DIR = Path(__file__).parent.parent / "data"
EXP_DIR = DATA_DIR / "All_subjects_spreadsheets"
OUTFILE = DATA_DIR / "concatenated.csv"


def main(input_dir: Path, outfile: Path):
    LOG.info(f"Loading from: {input_dir}")
    dfs = []
    for file in (pbar := tqdm(list(input_dir.iterdir()))):
        pbar.set_description(f"Loading {file.name}")
        if file.suffix == ".csv":
            df = pd.read_csv(file, header=None)
            # ^ header=None to avoid pandas inferring header from first row
            # because we actually want to repeat the header row on every other
            # row of the csv (an oddity due to downstream processing requirements).
            dfs.append(df)
    concatenated_df = pd.concat(dfs, ignore_index=True)

    LOG.info(f"Saving to: {outfile}")
    concatenated_df.to_csv(outfile, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge csv files.")
    parser.add_argument("--indir", help="input data dir", type=Path, default=EXP_DIR)
    parser.add_argument(
        "--outfile", help="output merged file", type=Path, default=OUTFILE
    )
    args = parser.parse_args()
    main(args.indir, args.outfile)
