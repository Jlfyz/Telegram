# coding=utf-8
# /home/jlfyz/PycharmProjects/Telegram/venv
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
        global i
        self.usernames = list_of_usernames
        self.channel = channel_to_add
        self.session = str(session_name)
        self.client = TelegramClient(
            self.session, constans.api_id, constans.api_hash,
            request_retries=1, connection_retries=1,
            flood_sleep_threshold=120
        )
        self.client.connect()
        if not self.client.is_user_authorized():
            phone_number = input('Please enter your phone (or bot token): ')
            self.client.send_code_request(phone_number)
            me = self.client.sign_in(phone_number, input('Enter code: '))
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
        try:
            self.channel = self.client.get_entity(self.channel)
            print('Channel to add is - '+str(self.channel))
            print('------------------------')
        except Exception as err:
            print(err)
            print('------------------------')
        print(self.usernames)
        print('------------------------')

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
                except telethon.errors.rpcerrorlist.UsernameInvalidError as err:
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.UserPrivacyRestrictedError as err:
                    print('>>>>0. UserPrivacyRestrictedError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.ChatAdminRequiredError as err:
                    print('>>>>1. ChatAdminRequiredError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.ChatIdInvalidError as err:
                    print('>>>>2. ChatIdInvalidError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.InputUserDeactivatedError as err:
                    print('>>>>3. InputUserDeactivatedError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.PeerIdInvalidError as err:
                    print('>>>>4. PeerIdInvalidError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.UserAlreadyParticipantError as err:
                    print('>>>>5. UserAlreadyParticipantError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.UserIdInvalidError as err:
                    print('>>>>6. UserIdInvalidError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.UserNotMutualContactError as err:
                    print('>>>>>7. UserNotMutualContactError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.UsersTooMuchError as err:
                    print('>>>>>8. UsersTooMuchError...')
                    print(err)
                    print('------------------------')
                except errors.rpcerrorlist.PeerFloodError as err:
                    print('>>>>>9. PeerFloodError try again in 24 Hours...Yes, you in spam')
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
            except errors.rpcerrorlist.UserPrivacyRestrictedError as err:
                print('>>>>0. UserPrivacyRestrictedError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.ChatAdminRequiredError as err:
                print('>>>>1. ChatAdminRequiredError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.ChatIdInvalidError as err:
                print('>>>>2. ChatIdInvalidError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.InputUserDeactivatedError as err:
                print('>>>>3. InputUserDeactivatedError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.PeerIdInvalidError as err:
                print('>>>>4. PeerIdInvalidError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.UserAlreadyParticipantError as err:
                print('>>>>5. UserAlreadyParticipantError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.UserIdInvalidError as err:
                print('>>>>6. UserIdInvalidError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.UserNotMutualContactError as err:
                print('>>>>>7. UserNotMutualContactError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.UsersTooMuchError as err:
                print('>>>>>8. UsersTooMuchError...')
                print(err)
                print('------------------------')
            except errors.rpcerrorlist.PeerFloodError as err:
                print('>>>>>9. PeerFloodError try again in 24 Hours...Yes, you in spam')
                print(err)
                print('------------------------')
                # sleep(86400)

    def disconnect(self):
        self.client.disconnect()
        print('Disconnecting from account. Closing session. Success!')
        print('------------------------')
