import json
import sys

from numbers_parser import Document

# script to convert a .numbers file with two columns (word, translation) to a plover JSON dict
numbers_file_path = sys.argv[1]
output_file_path = sys.argv[2]

doc = Document(numbers_file_path)
sheets = doc.sheets
tables = sheets[0].tables
rows = tables[0].rows(values_only=True)
translations = {}
for row in rows:
    if row[1]:
        translations[row[1].strip()] = row[0].strip()
with open(output_file_path, "w") as json_file:
    json.dump(dict(sorted(translations.items())), json_file, indent=0)
    json_file.write("\n")  # Add newline cause Py JSON does not
