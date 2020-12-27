# NearRest (TOC Project 2020)

![](https://i.imgur.com/S1GHFgf.png)

> The NearRest Line Bot!

---

## Introduction to this project

Search bset reviewed restaurant nearby you, add to your favorite list, view in Google Map, lookup the states. Line [button carousel templates](https://developers.line.biz/en/reference/messaging-api/#buttons) are used. Instead of typing bunch of word to the LINE bot, you can just simply **press buttons** on the carousel template!.

This LINE bot is mostly built by [LINE messaging API](https://developers.line.biz/en/docs/messaging-api/overview/), and a little [Flask](https://flask.palletsprojects.com/en/1.1.x/) as web application framework to host it on Heroku.

---

## How to Use
### 1. Open QR code scanner on your phone, and scan this following picture

![](https://i.imgur.com/E5nT1Ni.png)

### 2. Add NearRest to Your Friend

![](https://i.imgur.com/cBoYvw9.png)

---

## Features
### Search Restaurants Nearby
- Navigate to this Line bot chatroom
- Press the "Plus" icon at left bottom for sending advanced information to this bot

	![](https://i.imgur.com/zXBTnPZ.png)
- Click "位置資訊" and slide to location you want to search, then press the address to send it out

	![](https://i.imgur.com/KgIpvCw.png)

- Just wait a few second for API response, you will get a bunch of restaurants nearby!

	![](https://i.imgur.com/FGrahOS.png)


### Add to Favorite List
- Select some restaurants you intreseted in, then click "加入我的最愛" button in carousel templates.
- Type text message "List" (case-insensitive), bot will reply your favorite list
	![](https://i.imgur.com/hGPxvnx.png)

- You can also click "從最愛中移除" button to delete these items

### View in Google Map
- Click "到Google Map中查看", this location will be shown in Google Map App (if you installed this app on your phone)

### Lookup the States
- Type text message "Graph" (case-insensitive), bot will reply you an image about FSM of this bot.

	![](https://i.imgur.com/PnnNhrl.png)

## Technics Applied
### Google Map API for Place Search
![](https://i.imgur.com/CC21tCL.png)

### Firebase Realtime Database for Storing User Data
![](https://i.imgur.com/ImmdA2S.png)