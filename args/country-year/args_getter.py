# imports
import argparse

def get_args(argv=None): 
    parser = argparse.ArgumentParser(description="Get year and country")
    parser.add_argument('-c', '--country', help='add one country')
    parser.add_argument('-y', '--year', type=int, default= 1970, help='add a year')

    return parser.parse_args()