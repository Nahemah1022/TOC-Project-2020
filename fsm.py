# -*- coding: utf-8 -*-
import json

from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, PostbackEvent, TextSendMessage

from utils import send_text_message, send_image_url, send_carousel

from GoogleMaps import GoogleMaps
from Firestorage import Firestorage

class TocMachine(GraphMachine):
    def __init__(self):
        configs = json.load(open(f'./config.json'))
        print(configs)
        
        self.base_url = configs['base_url']
        self.gmap = GoogleMaps(configs['googlemap_api_key'])
        self.db = Firestorage(configs['firebase_url'])

        self.machine = GraphMachine(
            model=self, 
            states=["user", "postback", "nearby", "favorlist", "graph"],
            transitions=[
                {
                    "trigger": "advance",
                    "source": "user",
                    "dest": "postback",
                    "conditions": "is_going_to_postback",
                },
                {
                    "trigger": "advance",
                    "source": "user",
                    "dest": "nearby",
                    "conditions": "is_going_to_nearby",
                },
                {
                    "trigger": "advance",
                    "source": "user",
                    "dest": "favorlist",
                    "conditions": "is_going_to_favorlist",
                },
                {
                    "trigger": "advance",
                    "source": "user",
                    "dest": "graph",
                    "conditions": "is_going_to_graph",
                },
                {"trigger": "go_back", "source": ["postback", "nearby", "favorlist", "graph"], "dest": "user"},
            ],
            initial="user",
            auto_transitions=False,
            show_conditions=True,
        )

    def is_going_to_postback(self, event):
        return isinstance(event, PostbackEvent)

    def is_going_to_nearby(self, event):
        return isinstance(event, MessageEvent) and event.message.type == "location"

    def is_going_to_favorlist(self, event):
        return isinstance(event, MessageEvent) and event.message.type == "text" and event.message.text.lower() == "list"

    def is_going_to_graph(self, event):
        return isinstance(event, MessageEvent) and event.message.type == "text" and event.message.text.lower() == "graph"


    def on_enter_postback(self, event):
        print("I'm entering postback")

        place_id = event.postback.data.split(',')[0]
        place_name = event.postback.data.split(',')[1]
        mode = event.postback.data.split(',')[2]

        reply_token = event.reply_token
        print(mode)

        if mode == "put":
            self.db.add_to_favorite(event.source.user_id, place_id)
            send_text_message(reply_token, f"已將「{place_name}」加到我的最愛")
        else:
            self.db.remove_from_favorite(event.source.user_id, place_id)
            send_text_message(reply_token, f"已將「{place_name}」從我的最愛移除")

        self.go_back()

    def on_enter_nearby(self, event):
        print("I'm entering nearby")

        reply_token = event.reply_token
        send_carousel(reply_token, self.gmap.get_info(event.message.latitude, event.message.longitude))

        self.go_back()

    def on_enter_favorlist(self, event):
        print("I'm entering favorlist")

        favorites = self.db.get_user_favorite(event.source.user_id)
        carousel_list = [self.gmap.get_place_by_id(favorite) for favorite in favorites]

        reply_token = event.reply_token
        send_carousel(reply_token, carousel_list, True)

        self.go_back()

    def on_enter_graph(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token, self.base_url + '/show-fsm')
        self.go_back()


    def on_exit_postback(self):
        print("Leaving postback")

    def on_exit_nearby(self):
        print("Leaving nearby")

    def on_exit_favorlist(self):
        print("Leaving favorlist")

    def on_exit_graph(self):
        print("Leaving graph")
