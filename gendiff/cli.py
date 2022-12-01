import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser._optionals.title = "optional arguments"
    args = parser.parse_args()
    return args
