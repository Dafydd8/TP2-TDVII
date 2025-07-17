import csv
import json

def is_fully_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def convert(entity):
    f_in = open(f'csvs/{entity}.csv', 'r', encoding = 'utf-8')
    f_out = open(f'jsons/{entity}.json', 'w', encoding = 'utf-8')

    items = []
    reader = csv.DictReader(f_in)
    columns = reader.fieldnames
    print(f"Columns found: {columns}")
    for line in reader:
        for column in columns:
            if is_fully_int(line[column]):
                line[column] = int(line[column])
            else:
                line[column] = line[column].strip()
        items.append(line)

    json.dump(items, f_out, ensure_ascii=False, indent=2)
