import pandas as pd 
from func_args import get_args
from func_extract import extract
from func_transform import transform

import sys


def main(): 
    print('usando sys --- >', sys.argv)
    args = get_args()
    print(args.name)
    df = extract(args.name)
    print(df.columns)
    df = transform(df, args)
    print(df.columns)




if __name__ == "__main__": 
    main()