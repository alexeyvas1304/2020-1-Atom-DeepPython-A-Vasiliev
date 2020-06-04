import os
import datetime
import humanize
import xlwt


def walk(path, level):
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        if os.path.isfile(new_path) or os.path.isdir(new_path):
            abspath = os.path.abspath(new_path)
            size = humanize.naturalsize(os.stat(new_path).st_size)
            date_change = datetime.datetime.fromtimestamp(os.stat(new_path).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            info.append([name,
                         'f' if os.path.isfile(new_path) else 'd',
                         size,
                         date_change,
                         level,
                         abspath])
            if os.path.isdir(new_path):
                walk(new_path, level + 1)


def create_table():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Task Sheet')
    for i, record in enumerate(info):
        for j, value in enumerate(record):
            ws.write(i, j, value)
    wb.save('example.xls')


if __name__ == "__main__":
    level = 1
    info = [["Name", "Mark", "Size", "Date_change", "Level", "Abspath"]]
    path = input("Введите путь:")
    walk(path, level)
    create_table()
