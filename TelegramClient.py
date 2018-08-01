# coding=utf-8
from telethon.tl.types import InputChannel, InputUser, InputPhoneContact
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon import TelegramClient, sync,  errors
from time import sleep
import constans
import re


class TeleClient:
    def __init__(self, list_of_usernames, channel_to_add, session_name):
        """

        :param list_of_usernames:list
        :param channel_to_add:str
        :param session_name:str
        """
        self.usernames = list_of_usernames
        self.channel = channel_to_add
        self.session = str(session_name)
        self.client = TelegramClient(
            self.session, constans.api_id, constans.api_hash,
            timeout=timedelta(seconds=30), request_retries=1,
            connection_retries=1, flood_sleep_threshold=120
        )
        self.client.connect()
        if not self.client.is_user_authorized():
            phone_number = input('Please enter your phone (or bot token): ')
            self.client.send_code_request(phone_number)
            me = self.client.sign_in(phone_number, input('Enter code: '))
        for i in range(len(self.usernames)):
            self.usernames[i] = self.client.get_entity(self.usernames[i])
        self.channel = self.client.get_entity(self.channel)

    def add_contact(self):
        for i in range(len(self.usernames)):
            if not self.usernames[i].mutual_contact:
                contact = InputPhoneContact(
                                client_id=0,
                                phone=self.usernames[i].phone,
                                first_name=self.usernames[i].first_name,
                                last_name=self.usernames[i].last_name
                )
                self.client(ImportContactsRequest([contact]))

    def invite_to_channel(self):
        for i in range(len(self.usernames)):
            try:
                if self.usernames[i]:
                    sleep(31)
                    self.client(InviteToChannelRequest(InputChannel(
                        self.channel.id,
                        self.channel.access_hash), [InputUser(
                        self.usernames[i].id,
                        self.usernames[i].access_hash
                    )]
                    ))
                    sleep(5)
            except errors.rpcerrorlist.UserPrivacyRestrictedError as err:
                print('>>>>0. UserPrivacyRestrictedError...')
                print(err)
            except errors.rpcerrorlist.ChatAdminRequiredError as err:
                print('>>>>1. ChatAdminRequiredError...')
                print(err)
            except errors.rpcerrorlist.ChatIdInvalidError as err:
                print('>>>>2. ChatIdInvalidError...')
                print(err)
            except errors.rpcerrorlist.InputUserDeactivatedError as err:
                print('>>>>3. InputUserDeactivatedError...')
                print(err)
            except errors.rpcerrorlist.PeerIdInvalidError as err:
                print('>>>>4. PeerIdInvalidError...')
                print(err)
            except errors.rpcerrorlist.UserAlreadyParticipantError as err:
                print('>>>>5. UserAlreadyParticipantError...')
                print(err)
            except errors.rpcerrorlist.UserIdInvalidError as err:
                print('>>>>6. UserIdInvalidError...')
                print(err)
            except errors.rpcerrorlist.UserNotMutualContactError as err:
                print('>>>>>7. UserNotMutualContactError...')
                print(err)
            except errors.rpcerrorlist.UsersTooMuchError as err:
                print('>>>>>8. UsersTooMuchError...')
                print(err)
            except errors.rpcerrorlist.PeerFloodError as err:
                print('>>>>>9. PeerFloodError try again in 24 Hours...Yes, you in spam')
                print(err)
                # sleep(86400)

    def disconnect(self):
        self.client.disconnect()

