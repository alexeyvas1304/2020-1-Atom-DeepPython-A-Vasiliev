import os
import datetime
import humanize
import xlwt


def walk(path, level):
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        abspath = os.path.abspath(new_path)
        if os.path.isfile(new_path):
            mark = 'f'
            size = humanize.naturalsize(os.stat(new_path).st_size)
            date_change = datetime.datetime.fromtimestamp(os.stat(new_path).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            info.append([name, mark, size, date_change, level, abspath])
        elif os.path.isdir(new_path):
            mark = 'd'
            size = humanize.naturalsize(os.stat(new_path).st_size)
            date_change = datetime.datetime.fromtimestamp(os.stat(new_path).st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            info.append([name, mark, size, date_change, level, abspath])
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
