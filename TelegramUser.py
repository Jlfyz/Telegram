# coding=utf-8
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
