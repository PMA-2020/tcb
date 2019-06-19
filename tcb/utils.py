import argparse
import pprint

from . import get_question_numbers


PROG_HEADER = 'header'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper program')
    parser.add_argument(
        'program', choices=[PROG_HEADER],
        help=('Which utility to run. "header" creates the header from a '
              'template file')
    )
    parser.add_argument(
        '-i', '--input', help='Input file'
    )
    args = parser.parse_args()

    if args.program == PROG_HEADER:
        question_numbers = get_question_numbers(args.input)
        pprint.pprint(question_numbers, indent=4)
