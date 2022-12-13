import requests

class Mapquest:
  def __init__(self):
    '''
    stores url and client key
    '''
    self.url = "http://www.mapquestapi.com/geocoding/v1/address?"
    self.client_key = "6C2mLrXgy3N7RsfcdMsFR5ngaXJA0jQ9"
  def coords_get(self, location):
    '''
    returns coordinates of user's location
    '''
    self.req = requests.get(f'{self.url}key={self.client_key}&location={location}').json()
    self.lat = self.req['results'][0]['locations'][0]['latLng']['lat']
    self.long = self.req['results'][0]['locations'][0]['latLng']['lng']
   
    
      
    if self.long >= 0:
      return f'{self.lat}+{self.long}'
    if self.long <= 0:
      return f'{self.lat}{self.long}'