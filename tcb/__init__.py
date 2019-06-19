from collections import namedtuple
import re
import os.path
from typing import List

import xlrd


AssessmentSetup = namedtuple("AssessmentSetup", ["country", "person", "scorer"])
AssessmentRow = namedtuple('AssessmentRow', [
    'entry', 'relevancy', 'priority', 'score', 'notes'
])


class AssessmentItem:

    def __init__(
            self, assessment_setup: AssessmentSetup,
            assessment_row: AssessmentRow):
        self.assessment_setup = assessment_setup
        self.assessment_row = assessment_row


def generate_filename(assessment_setup: AssessmentSetup):
    ordered = [assessment_setup.person, assessment_setup.country,
               assessment_setup.scorer]
    stripped = [chunk.strip() for chunk in ordered]
    underscored = [chunk.replace(" ", "-") for chunk in stripped]
    underscored_again = [chunk.replace("_", "-") for chunk in underscored]
    undoubled = [_undouble_hyphen(chunk) for chunk in underscored_again]
    ascii_only = [_remove_non_ascii(chunk) for chunk in undoubled]
    basename = "_".join(ascii_only)
    filename = f"{basename}.xlsx"
    return filename


def _undouble_hyphen(text: str):
    while "--" in text:
        text = text.replace("--", "-")
    return text


def _remove_non_ascii(text: str):
    result = re.sub(r'[^a-zA-Z0-9-]+', '', text)
    return result


def extract_from_filename(filename: str):
    basename = os.path.basename(filename)
    root, _ = os.path.splitext(basename)
    # Raises ValueError not enough values to unpack if not named correctly
    person, country, scorer, *_ = root.split('_')
    return AssessmentSetup(country, person, scorer)


COL_ENTRY = 0
COL_DETAIL = 1
COL_RELEVANCY = 2
COL_PRIORITY = 3
COL_SCORE = 4
COL_NOTES = 5


SCORES_SHEET_NAME = 'individual'


class IndividualAssessment:

    def __init__(
            self, assessment_setup: AssessmentSetup,
            rows: List[AssessmentRow]):
        self.assessment_setup = assessment_setup
        self.rows = rows
        self.rows_by_entry = {
            row.entry: row for row in self.rows
        }
        self.country = self.assessment_setup.country

    def get(self, item: str):
        return self.rows_by_entry.get(item)

    def get_data_row(self, tcb_questions: List[str]):
        row = list(self.assessment_setup)
        for question in tcb_questions:
            assessment_row = self.get(question)
            if assessment_row:
                entry, *data = assessment_row
                row.extend(data)
            else:
                row.extend([None] * 4)
        return row

    @classmethod
    def from_file(cls, filename: str):
        assessment_setup = extract_from_filename(filename)
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_name(SCORES_SHEET_NAME)
        rows = sheet.get_rows()
        next(rows)
        assessment_rows = []
        for row in rows:
            entry = row[COL_ENTRY].value
            if not entry_is_scored(entry):
                continue
            relevancy = row[COL_RELEVANCY].value
            priority = row[COL_PRIORITY].value
            score = row[COL_SCORE].value
            notes = row[COL_NOTES].value
            assessment_row = AssessmentRow(
                entry, relevancy, priority, score, notes
            )
            assessment_rows.append(assessment_row)
        return cls(assessment_setup, assessment_rows)


def get_question_numbers(filename: str) -> List[str]:
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_name(SCORES_SHEET_NAME)
    entries = sheet.col_values(COL_ENTRY)
    filtered = filter(entry_is_scored, entries)
    return list(filtered)


def entry_is_scored(entry):
    found = re.match(r'[A-Z]\d+', str(entry))
    return bool(found)


def load_scores_from_xlsx(filename: str) -> IndividualAssessment:
    return IndividualAssessment.from_file(filename)
