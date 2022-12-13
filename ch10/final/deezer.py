import requests
import json
import random

class Deezer:
  def __init__(self):
    '''
    initializes deezer class
    no args/returns
    '''
    self.search_url = "https://api.deezer.com/search/artist?q="
    self.client_id =  "571362"
    self. client_secret = " ae7fcdbb085b4bb2a08a9a1b177559a1"
  def get_artist_id(self,artist):
    '''
    gets the artist id in order to look for the genre
    args: 
    artist: artist name
    '''
    self.r = requests.get(f'{self.search_url}{artist}')
    self.artist_list = (self.r.json())
    
    self.artist_id = self.artist_list['data'][0]['id']
    return self.artist_id
  def get_album_list(self,id):
    '''
    gets a list of albums and album genres
    args:
    id: artist id from previous function
    '''
    self.list_url  = f"https://api.deezer.com/artist/{id}/albums"
    al_list = requests.get(self.list_url)
    list_json = al_list.json()
    data = list_json['data']
    self.al_ids = []
    self.artist_genres = []
    for num in data:
      self.al_ids.append(num['id'])
    for album in self.al_ids:
      al_info = requests.get(f'https://api.deezer.com/album/{self.al_ids[0]}').json()
      # print(al_info['genres']['data'][0]['name'])
      self.artist_genres.append(al_info['genres']['data'][0]['name'])
  def pick_random(self):
    '''
    picks a random genre to recommend events
    returns a genre
    '''
    list_num = random.randrange(len(self.artist_genres)-1)
    random_gen =  str(self.artist_genres[list_num])
    r = random_gen.replace(" ","+")
    r = r.replace("/","+")
    print("Genre:",r.lower())
    return r.lower()
    
      
      
      