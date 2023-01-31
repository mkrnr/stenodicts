import sys

from numbers_parser import Document

doc = Document(sys.argv[1])
sheets = doc.sheets
tables = sheets[0].tables
rows = tables[0].rows(values_only=True)
for row in rows:
    if row[1]:
        print(f"| {row[1]} | {row[0]} |")
