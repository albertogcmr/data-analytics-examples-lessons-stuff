import argparse

def get_args(argv=None):
    valid_bootcamps = ['web', 'uxui', 'data']

    parser = argparse.ArgumentParser(description="Arguments for Hiring Fair")
    parser.add_argument("bootcamp", type=str, choices=valid_bootcamps, help="[web, uxui or data]")
    parser.add_argument("companiesCSV", type=str, help="Relative path to companies survey CSV")
    parser.add_argument("studentsCSV", type=str, help="Relative path to students survey CSV")
    parser.add_argument("rounds", type=int, help="Max rounds per hiring fair")    # ...
    return parser.parse_args(argv)

def main():

    args = get_args()
    print(args.bootcamp, args.companiesCSV, args.studentsCSV, args.rounds)

if __name__ == '__main__':
    main()