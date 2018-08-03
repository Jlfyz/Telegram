# coding=utf-8
import csv
counter = 0
tmp_list = []
channel = input('Link of channel pls, example: https://t.me/qwertyuiop1234567890 ')
print('------------------------')
print('Temporary list is opened')
print('------------------------')
with open('usernames.csv') as f:
    len_of_file = sum(1 for _ in f)
    f.close()
with open('usernames.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print('Reading file')
    print('------------------------')
    for row in csv_reader:
        tmp = [row[0][1:].replace('\n', ''), row[1]]
        print(tmp)
        print('------------------------')
        tmp_list.append(tmp)
        print(tmp_list)
        print('------------------------')
print(tmp_list[0][0])
print(tmp_list[10][0])
