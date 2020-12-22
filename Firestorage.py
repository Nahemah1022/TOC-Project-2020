# -*- coding: utf-8 -*-

import requests
from firebase import firebase

class Firestorage:
    def __init__(self, base):
        self.fb_app = firebase.FirebaseApplication(base, None)

    def add_to_favorite(self, name, place_id):
        favorite = self.get_user_favorite(name)
        if place_id not in favorite:
            favorite.append(place_id)
            self.fb_app.put('/users', name=name, data={"favorite": favorite})

    def remove_from_favorite(self, name, place_id):
        favorite = self.get_user_favorite(name)
        if place_id in favorite:
            favorite.remove(place_id)
            self.fb_app.put('/users', name=name, data={"favorite": favorite})

    def get_user_favorite(self, name):
        return self.fb_app.get('/users', name)['favorite'] if self.fb_app.get('/users', name) != None else []

if __name__ == '__main__':
    f = Firestorage()
    print(f.add_to_favorite('Nahemah', 'ChIJ5xiczMB2bjQRQRQdAfHxpMQ'))
