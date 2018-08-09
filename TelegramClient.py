# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
from telethon.tl.types import ChannelForbidden, ChatEmpty, ChatForbidden, InputChannel, InputUser, InputPhoneContact
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import TelegramClient, sync, errors
from time import sleep
import constans
import os
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
        self.flag_user = False
        self.flag_channel = False
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
        """
        :param list_of_usernames:list

        Define User by getting entity from username
        """
        self.flag_user = True
        self.usernames = list_of_usernames
        i = 0
        while i < len(self.usernames):
            try:
                self.usernames[i][0] = self.client.get_entity(self.usernames[i][0])
                """[0]"""
                print(str(self.usernames[i][0]) + ' new entity')
                print('------------------------')
                i += 1
            except Exception as err:
                print(i)
                del self.usernames[i]
                print(len(self.usernames))
                print(err)
                print('------------------------')
        print(self.usernames)
        print('------------------------')

    def def_channel(self, channel_to_add):
        """

        :param channel_to_add:str(url of channel or supergroup)
        :return:bool:Democracy of Channel

        Define channel by getting entity from url and returns boolean variable
        Democracy
        If Democracy is True use def add_contact()
        Else use def self_add_channel()//it's working in my TelegramUser.py file
        """
        self.flag_channel = True
        self.channel = channel_to_add
        try:
            self.channel = self.client.get_entity(self.channel)
            print('Channel to add is - '+str(self.channel))
            print('------------------------')
            if self.channel.democracy:
                print('Democracy is True')
                print('------------------------')
                return True
            else:
                print('Democracy is False')
                print('------------------------')
                return False
        except Exception as err:
            print(err)
            print('------------------------')

    def self_add_channel(self):
        """
        First time you use this with passwords and it's saving to .session file,
        Second time u don't need any log in,
        do not use it without def_channel().
        """
        if not self.flag_channel:
            try:
                sleep(31)
                self.client(JoinChannelRequest(self.channel))
            except Exception as err:
                print(err)
        else:
            print('You don\'t define channel try again')

    def add_contact(self):
        """

        This definition adding contact to your contact list to become mutual contact,
        do not use it without def_usernames().
        """
        if self.flag_user:
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
        else:
            print('You don\'t define users to add, please try again')

    def invite_to_channel(self):
        """

        This definition adding contact to group,
        do not use it without def_channel() and def_usernames().
        You can invite to channel from 1 session max 15 people after that you are at risk.
        You can be banned because too many requests from 1 session.
        """
        if self.flag_channel and self.flag_user:
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
        else:
            print('You don\'t define channel and users to add, please try again')

    def disconnect(self):
        """

        Disconnecting from Telegram to open new session
        """
        self.client.disconnect()
        print('Disconnecting from account. Closing session. Success!')
        print('------------------------')
