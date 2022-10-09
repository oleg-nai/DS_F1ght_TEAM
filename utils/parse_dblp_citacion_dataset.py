import numpy as np # linear algebra
import pandas as pd


import ijson
from tqdm import tqdm
import pprint
pp = pprint.PrettyPrinter(width=180).pprint
import gc


def get_all_colnames():
    return ['authors',  'year']


def get_datalist(n=300_000, colnames=None):
    colnames = colnames if colnames else get_all_colnames()
    datalist = list()
    with open("data/dblpv13.json", "rb") as f:
        for i, element in enumerate(tqdm(ijson.items(f, "item"))):
            paper = {colname: element.get(colname, np.nan) for colname in colnames}
            datalist.append(paper)
            if i == n:
                break
    return datalist


def main():
    datalist = get_datalist()
    df = pd.DataFrame(datalist)
    df.to_csv('authors_year.csv')
    del datalist
    gc.collect()


if __name__ == '__main__':
    main()
