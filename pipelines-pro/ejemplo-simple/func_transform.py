import pandas as pd

def f1(df): 
    return df

def f2(df): 
    return df

def f3(df, args): 
    return df.drop(args.column, axis=1)

def transform(df, args): 
    df = f1(df) 
    df = f2(df) 
    df = f3(df, args) 
    return df

print('estamos en transform 1')

if __name__ == "__main__": 
    print('estamos en transform 2')
