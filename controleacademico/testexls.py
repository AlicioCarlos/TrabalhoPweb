import xlsxwriter
import io
from django.utils.translation import ugettext
import string

def WriteToExcel(data):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Summary")
    keys = ['aluno', 'turma', 'nota1', 'nota2', 'nota3']

    description_col_width = 5
    observations_col_width = 25

    # excel styles

    title_text = ugettext('Relatório')
    # merge cells
    worksheet_s.merge_range('D2:E2', title_text)

    # write header
    worksheet_s.write(4, 0, ugettext("ID"))
    for key in keys:
        if len(key) > description_col_width:
            worksheet_s.set_column(4, keys.index(key) + 1, len(key))
        worksheet_s.write(4, keys.index(key) + 1, ugettext(string.capwords(key)))

    # add data to the table
    print(data)
    for idx, data in enumerate(data):
        row = 5 + idx
        worksheet_s.write_number(row, 0, idx + 1)
        for column in keys:
            data_column = data[column]
            if isinstance(data_column, int) or isinstance(data_column, float):
                worksheet_s.write_number(row, keys.index(column) + 1, data_column)
            else:
                tam_column = len(data[column])
                worksheet_s.write_string(row, keys.index(column) + 1, data_column) # Observations column
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data