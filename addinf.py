import json
import openpyxl

def tabl():
    book = openpyxl.open("students.xlsx", read_only=True)
    sheet = book.active

    for row in range(2, sheet.max_row + 1):
        i = sheet[row][0].value
        m = sheet[row][1].value
        r = sheet[row][2].value
        p = sheet[row][3].value
        e = sheet[row][4].value

        new_data = {'id': i,
                    'Mat': 'Математика - баллы/часы: %s;' % m,
                    'Rus': 'Математика - баллы/часы: %s;' % r,
                    'Prog': 'Математика - баллы/часы: %s;' % p,
                    'epsents': 'Колво-пропусков: %s' % e}
        with open('students.json', encoding='utf8') as k:
            data = json.load(k)
            data['student'].append(new_data)
            with open('students.json', 'w', encoding='utf8') as outline:
                json.dump(data, outline, ensure_ascii=False, indent=5)



