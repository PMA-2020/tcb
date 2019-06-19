import argparse
import os
import shutil
from typing import List

import xlrd

from . import AssessmentSetup, generate_filename


def create_files(
        template_assessment: str, personnel_file: str, output_dir: str) -> int:
    assessment_setup = get_assessment_setup_data(personnel_file)
    count_created = create_files_from_setup_data(
        template_assessment, assessment_setup, output_dir)
    return count_created


def create_files_from_setup_data(
        template_assessment: str, assessment_setup: List[AssessmentSetup],
        output_dir: str) -> int:
    count_created = 0
    if os.path.isfile(template_assessment):
        os.makedirs(output_dir, exist_ok=True)
        for item in assessment_setup:
            filename = generate_filename(item)
            full_filename = os.path.join(output_dir, filename)
            shutil.copy(template_assessment, full_filename)
            count_created += 1
    return count_created


COL_COUNTRY = 0
COL_PERSON = 1
COL_SCORER = 2


def get_assessment_setup_data(personnel_file: str) -> List[AssessmentSetup]:
    result = []
    book = xlrd.open_workbook(personnel_file)
    sheet = book.sheet_by_index(0)
    rows = sheet.get_rows()
    next(rows)
    for row in rows:
        country = row[COL_COUNTRY].value
        person = row[COL_PERSON].value
        scorer = row[COL_SCORER].value
        result.append(AssessmentSetup(country, person, scorer))
    return result


def main():
    parser = argparse.ArgumentParser(
        description='Create copies of template files and name them correctly'
    )
    parser.add_argument(
        '-t', '--template', required=True, help='Template file'
    )
    parser.add_argument(
        '-p', '--personnel', required=True,
        help=('File with the people participating in the TCB quantitative '
              'assessment')
    )
    parser.add_argument(
        '-o', '--output', default='output',
        help=('A directory where to save the created files. Defaults to '
              '"output" in the current directory')
    )
    args = parser.parse_args()
    count_created = create_files(args.template, args.personnel, args.output)
    print(f'Created {count_created} file(s) in directory "{args.output}"')

if __name__ == '__main__':
    main()
