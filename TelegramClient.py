# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
from typing import List, Any, Union, Coroutine

from telethon.tl.types import InputChannel, InputUser, InputPhoneContact, ChannelForbidden, ChatForbidden, ChatEmpty
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient, sync,  errors
from time import sleep
import constans
import re


class TeleClient:

    def __init__(self, session_name, proxy=None):
        """

        :param list_of_usernames:list
        :param channel_to_add:str
        :param session_name:str
        """
        global i
        self.usernames = []
        self.channel = ''
        self.session = str(session_name)
        self.proxy = proxy
        self.client = TelegramClient(
            self.session, constans.api_id, constans.api_hash,
            request_retries=1, connection_retries=1,
            flood_sleep_threshold=120, connection=ConnectionHttp,
            proxy=proxy
        )
        self.client.connect()
        if not self.client.is_user_authorized():
            phone_number = input('Please enter your phone (or bot token): ')
            self.client.send_code_request(phone_number)
            me = self.client.sign_in(phone_number, input('Enter code: '))

    def def_usernames(self, list_of_usernames):
        self.usernames = list_of_usernames
        i = 0
        while i < len(self.usernames):
            try:
                self.usernames[i][0] = self.client.get_entity(self.usernames[i])
                """[0]"""
                print(str(self.usernames[i][0]) + ' new entity')
                print('------------------------')
                i += 1
            except Exception as err:
                print(i)
                del self.usernames[i]
                i = 0
                print(len(self.usernames))
                print(err)
                print('------------------------')
        print(self.usernames)
        print('------------------------')

    def def_channel(self, channel_to_add):
        self.channel = channel_to_add
        try:
            self.channel = self.client.get_entity(self.channel)
            print('Channel to add is - '+str(self.channel))
            print('------------------------')
        except Exception as err:
            print(err)
            print('------------------------')
        if self.channel.democracy:
            print('Democracy is True')
            print('------------------------')
            return True
        else:
            print('Democracy is False')
            print('------------------------')
            return False

    def self_add_channel(self):
        try:
            self.client(JoinChannelRequest(self.channel))
        except Exception as err:
            print(err)

    def add_contact(self):
        for i in range(len(self.usernames)):
            if not self.usernames[i][0].mutual_contact:
                try:
                    """[1]"""
                    contact = InputPhoneContact(
                                    client_id=0,
                                    phone=self.usernames[i][1],
                                    first_name=self.usernames[i][0].first_name,
                                    last_name=self.usernames[i][0].last_name
                    )
                    self.client(ImportContactsRequest([contact]))
                    print('Successfully added '+str(contact)+' to your contact\'s')
                    print('------------------------')
                except Exception as err:
                    print(err)
                    print('------------------------')

    def invite_to_channel(self):
        for i in range(len(self.usernames)):
            try:
                if self.usernames[i][0]:
                    sleep(31)
                    self.client(InviteToChannelRequest(InputChannel(
                        self.channel.id,
                        self.channel.access_hash), [InputUser(self.usernames[i][0].id,
                                                              self.usernames[i][0].access_hash
                                                              )]
                    ))
                    print('Successfully added ' + str(self.usernames[i][0]) + ' to '+str(self.channel))
                    print('------------------------')
                    sleep(5)
            except Exception as err:
                print(err)
                print('------------------------')

    def disconnect(self):
        self.client.disconnect()
        print('Disconnecting from account. Closing session. Success!')
        print('------------------------')
