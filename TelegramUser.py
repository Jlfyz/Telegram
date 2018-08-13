# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
import TelegramClient
import socks
import csv


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
    print('Its test of democracy of channel')
    if test.def_channel(channel):
        test.disconnect()
        print('------------------------')
        print('Temporary list is opened')
        print('------------------------')
        with open('usernames.csv') as f:
            len_of_file = sum(1 for _ in f)
            f.close()
        with open('usernames.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
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
                if 15 == len(tmp_list) or counter == len_of_file:
                    client = TelegramClient.TeleClient(
                        counter
                    )
                    client.def_usernames(tmp_list)
                    client.def_channel(channel)
                    client.add_contact()
                    client.invite_to_channel()
                    client.disconnect()
                    print('Success')
                    print('------------------------')
                    tmp_list = []
                    print('Temporary list is refreshed')
                    print('------------------------')
        print('Temporary list is closed')
        print('------------------------')
        print('End of program')
        print('------------------------')
    else:
        test.disconnect()
        while True:
            try:
                counter = int(input('Sum of users to add'))
                break
            except Exception as err:
                print(err)
                print('------------------------')
                continue
        with open('proxy.csv') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            print('Reading proxy file')
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
                if wait_counter == 6:
                    wait_counter = 0
                    input('You have time to use another sim cards')
                    print('------------------------')
                for iterator in range(len(proxies)):
                    session = '{0}_autoadd'.format(str(i))
                    client = TelegramClient.TeleClient(
                        session,
                        proxies[iterator]
                    )
                    client.def_channel(channel)
                    client.self_add_channel()
                    client.disconnect()
                    print('Success')
                    print('------------------------')
                    print(i)
                    if i + 1 <= counter:
                        i += 1
                    else:
                        break
                    wait_counter += 1
        print('End of program')
        print('------------------------')


if __name__ == '__main__':
    main()

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