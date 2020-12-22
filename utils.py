# -*- coding: utf-8 -*-

import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    return "OK"

def send_carousel(reply_token, info, isList=False):
    
    columns = []
    for information in info:
        columns.append(
            CarouselColumn(
                thumbnail_image_url = information['preview_url'],
                title = information['name'],
                text = str(information['rating']) + "  (" + str(information['user_ratings_total']) + ")",
                actions = [
                    URIAction(
                        label = '到 Google Map 中查看',
                        uri = 'https://maps.google.com/?q=' + information['name']
                    ),
                    PostbackAction(
                        label = '加入我的最愛' if not isList else '從我的最愛移除',
                        data = information['place_id'] + "," + information['name'] + (",put" if not isList else ",delete")
                    )
                ]
            )
        )
    try:
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, TemplateSendMessage(
            alt_text = '附近的餐廳...',
            template = CarouselTemplate(columns=columns)
        ))
    except Exception as ex:
        print("Exception")
        print(ex)

    return "OK"
