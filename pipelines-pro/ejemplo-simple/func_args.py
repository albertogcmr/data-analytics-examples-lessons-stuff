import argparse

def get_args(): 
    parser = argparse.ArgumentParser(description="path to csv")
    parser.add_argument("-n", "--name", type=str)
    parser.add_argument("-c", "--column", type=str)
    return parser.parse_args()
