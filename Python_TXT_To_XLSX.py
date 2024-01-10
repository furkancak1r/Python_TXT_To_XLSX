from openpyxl import Workbook
# Converts a text file to an Excel file
def txt_to_xlsx(file_path, delimiter='\t', output_file='output.xlsx'):
    wb = Workbook()
    ws = wb.active

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into cells using the specified delimiter
            cells = line.strip().split(delimiter)
            ws.append(cells)

    wb.save(output_file)

# Example usage
txt_to_xlsx("C:\\Users\\furkan.cakir\\Desktop\\FurkanPRS\\Kodlar\\SSH\\1.txt")
