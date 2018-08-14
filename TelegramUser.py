# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
import TelegramClient
import socks
import csv

"""
This program using telegram client tools that working with telethon library

When the program starts You need to test the channel to which you need to add
users, if channel's democracy is true program starts to add users from usernames.csv
by portions, but you need to be on this channel,
if channel's democracy is false program choose another path, selfadding to channel
with proxies in file porxy.csv, after 6 persons u need to change sim cards
"""


def main():
    counter = 0
    tmp_list = []
    channel = input('Link of channel pls, example: https://t.me/qwertyuiop1234567890 ')
    """
    We need to check democracy of channel
    """
    test = TelegramClient.TeleClient(
                    'Test'
                )
    print('It\'s test of democracy of channel/Это тест приватности канала ')
    if test.def_channel(channel):
        delimiter = input('Enter delimiter/Введите знак который разделяет ячейки таблицы \' \',\',\' ')
        test.disconnect()
        print('------------------------')
        print('Temporary list is opened/Временный список открыт ')
        print('------------------------')
        with open('usernames.csv') as f:
            len_of_file = sum(1 for _ in f)
            f.close()
        with open('usernames.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            print('Reading file/Читаем файл ')
            print('------------------------')
            for row in csv_reader:
                tmp = [row[0][1:].replace('\n', ''), row[1]]
                print(tmp)
                print('------------------------')
                tmp_list.append(tmp)
                print(tmp_list)
                print('------------------------')
                counter += 1
                if 15 == len(tmp_list) or counter == len_of_file:
                    client = TelegramClient.TeleClient(
                        counter
                    )
                    client.def_usernames(tmp_list)
                    client.def_channel(channel)
                    client.add_contact()
                    client.invite_to_channel()
                    client.disconnect()
                    print('Success/Успех ')
                    print('------------------------')
                    tmp_list = []
                    print('Temporary list is refreshed/Временный список обнулён ')
                    print('------------------------')
        i = 0
        while i < counter:
            try:
                os.remove("{0}.session".format(str(i)))
                print("File Removed!/Файл успешно удалён")
                i += 1
            except Exception as err:
                i += 1
        print('Temporary list is closed/Временный список закрыт ')
        print('------------------------')
        print('End of program/Конец программы ')
        print('------------------------')
    else:
        test.disconnect()
        while True:
            try:
                counter = int(input('Sum of users to add/Кол-во пользователей которых надо добавить '))
                phone_counter = int(input('Sum of phones you have/Сколько сим карт может быть одновременно '
                                          'задейственно? '))
                break
            except Exception as err:
                print(err)
                print('------------------------')
                continue
        delimiter = input('Enter delimiter/Введите знак который разделяет ячейки таблицы \' \',\',\' ')
        with open('proxy.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            print('Reading proxy file/Читаем прокси файл ')
            print('------------------------')
            wait_counter = 0
            proxies = []
            for row in csv_reader:
                proxies.append((socks.HTTP, row[0], int(row[1]), True,
                                row[2], row[3]
                                ))
            print(proxies)
            i = 0
            while i < counter:
                if counter < len(proxies):
                    for iterator in range(counter):
                        if wait_counter == phone_counter:
                            wait_counter = 0
                            input('You have time to use another sim cards/У вас есть время заменить сим карты ')
                            print('------------------------')
                        session = '{0}_autoadd'.format(str(i))
                        client = TelegramClient.TeleClient(
                            session,
                            proxies[iterator]
                        )
                        client.def_channel(channel)
                        client.self_add_channel()
                        client.disconnect()
                        print('Success/Успех ')
                        print('------------------------')
                        print(i)
                        if i + 1 <= counter:
                            i += 1
                        else:
                            break
                        wait_counter += 1
                    else:
                        for iterator in range(len(proxies)):
                            if wait_counter == phone_counter:
                                wait_counter = 0
                                input('You have time to use another sim cards/У вас есть время заменить сим карты ')
                                print('------------------------')
                            session = '{0}_autoadd'.format(str(i))
                            client = TelegramClient.TeleClient(
                                session,
                                proxies[iterator]
                            )
                            client.def_channel(channel)
                            client.self_add_channel()
                            client.disconnect()
                            print('Success/Успех ')
                            print('------------------------')
                            print(i)
                            if i + 1 <= counter:
                                i += 1
                            else:
                                break
                            wait_counter += 1
        i = 0
        while i < counter:
            try:
                os.remove("{0}_autoadd.session".format(str(i)))
                print("File Removed!/Файл успешно удалён ")
                i += 1
            except Exception as err:
                print(err)
                i += 1
        print('End of program/Конец программы ')
        print('------------------------')


if __name__ == '__main__':
    main()

