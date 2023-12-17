import config as auth
import requests
import vk_api as vk
from ..models.sender import Sender
from vk_api.keyboard import VkKeyboard


class VkSender(Sender):

    def login(self):
        api = vk.VkApi(token=auth.tokenVk)
        self.bot = api.get_api()

    def send(self):
        for member in self.members:
            self.bot.messages.send(peer_id=member, message=self.message, random_id=0,
                                   keyboard=self.keyboard.get_keyboard())

    def create_message(self, message: str = '', link: str = '', button: str = ''):
        self.keyboard = VkKeyboard()

        response = requests.get(
            "https://api.vk.com/method/groups.getMembers",
            params={
                'access_token': auth.tokenVk,
                'v': 5.154,
                'group_id': 223879878,
                'count': 1000
            }
        )

        self.keyboard.add_openlink_button(button, link)
        self.message = message
        self.members = response.json()['response']['items']
