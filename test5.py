from openpyxl import load_workbook

wb = load_workbook('test5.xlsx')
sheet = wb.active

sheet.append(['name', 'price'])

wb.save('test5.xlsx')

