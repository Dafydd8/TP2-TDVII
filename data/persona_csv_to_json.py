import csv
import json

f_in = open('persona.csv', 'r', encoding = 'utf-8')
f_out = open('persona.json', 'w', encoding = 'utf-8')

personas = []
for line in csv.DictReader(f_in):
    line['numero_documento'] = int(line['numero_documento'])
    line['id_provincia'] = int(line['id_provincia'])
    personas.append(line)

json.dump(personas, f_out, ensure_ascii=False, indent=2)
