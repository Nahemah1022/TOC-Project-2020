# -*- coding: utf-8 -*-

import requests
import re

class GoogleMaps():
    def __init__(self, key):
        self.key = key

    def get_info(self, latitude, longitude):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        payload = {
            'location': str(latitude) + ', ' + str(longitude),
            'radius': '1000',
            'types': 'restaurant',
            'key': self.key
        }
        res = requests.get(url, payload)

        results = []
        for location in res.json()['results']:
            if 'opening_hours' in location and location['opening_hours']['open_now']:
                results.append({
                    'name': re.sub('\W+', '', location['name']).replace(chr(160), " ")[:30],
                    'place_id': location['place_id'],
                    'preview_url': self.get_photo(location['photos'][0]['photo_reference']).replace(chr(160), " "),
                    'rating': location['rating'],
                    'user_ratings_total': location['user_ratings_total']
                })

        results = sorted(results, key=lambda item: item['rating'], reverse=True)
        return results[:10]


    def get_photo(self, reference):
        url = "https://maps.googleapis.com/maps/api/place/photo"
        payload = {
            'photoreference': reference,
            'key': self.key,
            'maxwidth': '1500'
        }
        res = requests.get(url, payload)
        return res.url

    def get_place_by_id(self, id):
        url = "https://maps.googleapis.com/maps/api/place/details/json"
        payload = {
            'place_id': id,
            'fields': 'name,photo,rating,user_ratings_total',
            'key': self.key
        }
        res = requests.get(url, payload)
        result = res.json()['result']
        return {
            'name': re.sub('\W+', '', result['name']).replace(chr(160), " "),
            'preview_url': self.get_photo(result['photos'][0]['photo_reference']).replace(chr(160), " "),
            'rating': result['rating'],
            'user_ratings_total': result['user_ratings_total'],
            'place_id': id
        }


if __name__ == '__main__':
    g = GoogleMaps()
    print(g.get_place_by_id('ChIJ5xiczMB2bjQRQRQdAfHxpMQ'))