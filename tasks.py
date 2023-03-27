from app import celery



@celery.task
def run_hello():
    import time
    for i in range(1, 1000):
        time.sleep(2)
        print("Hello", i)
    return


run_hello()


# function use to download excel
def handle_excel(filename):
    import xlrd
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows
    cols = sheet.ncols
    data = []
    for i in range(1, rows):
        row = []
        for j in range(1, cols):
            row.append(sheet.cell_value(i, j))
        data.append(row)
    return data

# generate a function to download file excel
# return a binary file
