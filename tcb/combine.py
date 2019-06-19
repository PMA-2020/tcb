import argparse
from collections import defaultdict
import glob
import os.path
from typing import List

import xlsxwriter

from . import IndividualAssessment, load_scores_from_xlsx
from .tcb_questions import TCB_QUESTIONS


def combine_files(input_dir: str, output: str, by_country: bool):
    xlsx_files = glob.glob(os.path.join(input_dir, '*.xlsx'))
    all_assessments = []
    for xlsx_file in xlsx_files:
        individual_scores = load_scores_from_xlsx(xlsx_file)
        all_assessments.append(individual_scores)
    if by_country and all_assessments:
        write_by_country(all_assessments, output)
    else:
        write_all_together(all_assessments, output)


def write_by_country(
        all_assessments: List[IndividualAssessment], output: str):
    assessments_by_country = defaultdict(list)
    for assessment in all_assessments:
        assessments_by_country[assessment.country].append(assessment)
    workbook = xlsxwriter.Workbook(output)
    header_row = get_header_row()
    for key, values in sorted(assessments_by_country.items()):
        worksheet = workbook.add_worksheet(name=key)
        worksheet.write_row(0, 0, header_row)
        for i, assessment in enumerate(values, start=1):
            data_row = assessment.get_data_row(TCB_QUESTIONS)
            worksheet.write_row(i, 0, data_row)
    workbook.close()


def write_all_together(
        all_assessments: List[IndividualAssessment], output: str):
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write_row(0, 0, get_header_row())
    for i, assessment in enumerate(all_assessments, start=1):
        data_row = assessment.get_data_row(TCB_QUESTIONS)
        worksheet.write_row(i, 0, data_row)
    workbook.close()


def get_header_row():
    header = ['Country', 'Person', 'Scorer']
    for question in TCB_QUESTIONS:
        header.append(f'{question}_relevancy')
        header.append(f'{question}_priority')
        header.append(f'{question}_score')
        header.append(f'{question}_notes')
    return header


def main():
    parser = argparse.ArgumentParser(
        description='Combine results from TCB assessments into one file'
    )
    parser.add_argument(
        'input', help='A directory where to find assessment results'
    )
    parser.add_argument(
        '-o', '--output', default='tcb_results.xlsx',
        help=('A filename for the results. Defaults to '
              '"tcb_results.xlsx" in the current directory')
    )
    parser.add_argument(
        '-c', '--country', action='store_true',
        help=('Break the results up by country, so that each country has its '
              'own tab in the Excel file. Default is to combine all countries '
              'into one tab.')
    )
    args = parser.parse_args()
    combine_files(args.input, args.output, args.country)
    print(f'Wrote data to "{args.output}"')


if __name__ == '__main__':
    main()
