import argparse

"""
$ python3 args-example-pro.py web companies.csv students.csv 14
$ python3 args-example-pro.py -x parametronuevo web companies.csv students.csv 14
"""
def get_args(argv=None):
    valid_bootcamps = ['web', 'uxui', 'data']

    parser = argparse.ArgumentParser(description="Arguments for Hiring Fair")
    # parser.add_argument("-x", "--xxx", type=str,)
    parser.add_argument("bootcamp", type=str, choices=valid_bootcamps, help="[web, uxui or data]")
    parser.add_argument("companiesCSV", type=str, help="Relative path to companies survey CSV")
    parser.add_argument("studentsCSV", type=str, help="Relative path to students survey CSV")
    parser.add_argument("rounds", type=int, help="Max rounds per hiring fair")    # ...
    return parser.parse_args(argv)


def main():
    args = get_args()
    # print(args.xxx, args.bootcamp, args.companiesCSV, args.studentsCSV, args.rounds)
    print(args.bootcamp, args.companiesCSV, args.studentsCSV, args.rounds)


if __name__ == '__main__':
    main()