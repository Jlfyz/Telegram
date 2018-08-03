# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
"""
import TelegramClient


def spliting(array, size):
    arrays = []
    while len(array) > size:
        pice = array[:size]
        arrays.append(pice)
        array = array[size:]
    arrays.append(array)
    return arrays


def main():
    list_of_usernames = []
    with open('im.txt') as f:
        list_of_usernames = f.read().replace()
    new_arrs = spliting(list_of_usernames, 15)
    counter_of_loops = len(new_arrs)
    for i in range(counter_of_loops):
        clienti = TelegramClient.TeleClient(
            new_arrs[i],
            input('Link of channel pls, example: https://t.me/qwertyuiop1234567890'),
            i
        )
        clienti.add_contact()
        clienti.invite_to_channel()
        clienti.disconnect()


if __name__ == '__main__':
    main()
"""
import TelegramClient
import csv
"""
def main():
    counter = 0
    tmp_list = []
    channel = input('Link of channel pls, example: https://t.me/qwertyuiop1234567890 ')
    print('------------------------')
    print('Temporary list is opened')
    print('------------------------')
    with open('im.txt') as f:
        len_of_file = sum(1 for _ in f)
        f.close()
    with open('im.txt') as f:
        print('Reading file')
        print('------------------------')
        for line in f:
            tmp = line[1:].replace('\n', '')
            print(tmp)
            print('------------------------')
            tmp_list.append(tmp)
            print(tmp_list)
            print('------------------------')
            counter += 1
            if len(tmp_list) == 15 or len_of_file == counter:
                clienti = TelegramClient.TeleClient(
                    tmp_list,
                    channel,
                    counter
                )
                clienti.add_contact()
                clienti.invite_to_channel()
                clienti.disconnect()
                print('Success')
                print('------------------------')
                tmp_list = []
                print('Temporary list is refreshed')
                print('------------------------')
    print('Temporary list is closed')
    print('------------------------')
    print('End of program')
    print('------------------------')
"""


def main():
    counter = 0
    tmp_list = []
    channel = input('Link of channel pls, example: https://t.me/qwertyuiop1234567890 ')
    print('------------------------')
    print('Temporary list is opened')
    print('------------------------')
    with open('fff.csv') as f:
        len_of_file = sum(1 for _ in f)
        f.close()
    with open('fff.csv') as csvfile:
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
            counter += 1
            if len(tmp_list) == 15 or len_of_file == counter:
                clienti = TelegramClient.TeleClient(
                    tmp_list,
                    channel,
                    counter
                )
                clienti.add_contact()
                clienti.invite_to_channel()
                clienti.disconnect()
                print('Success')
                print('------------------------')
                tmp_list = []
                print('Temporary list is refreshed')
                print('------------------------')
    print('Temporary list is closed')
    print('------------------------')
    print('End of program')
    print('------------------------')


if __name__ == '__main__':
    main()

