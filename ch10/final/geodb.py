import requests

class GeoDB:
  def __init__(self,coords):
    '''
    stores url
    args:
    coords: coordinates of user
    '''
    # self.api_url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/locations/{coords}/nearbyCities?"
    self.url = f"https://wft-geo-db.p.rapidapi.com/v1/geo/locations/{coords}/nearbyCities"
  def get_nearest_city(self):
    '''
    uses coordinates to find the nearest city
    returns nearest city
    '''
    querystring = {"radius":"100",
                  "minPopulation":"40000",
                  }

    headers = {
	"X-RapidAPI-Key": "6cb5e47632msh00644aed9d13e28p11c69fjsnc7f2cf59503c",
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

    response = requests.request("GET", self.url, headers=headers, params=querystring).json()
    
    return response["data"][0]['name']