from mapquest import Mapquest
from deezer import Deezer
from geodb import GeoDB
from seatgeek import SeatGeek
def main():
  deezer_ = Deezer()
  mapq = Mapquest()
  seat = SeatGeek()
  
  chosen_artist = input("Give name of artist: ")
  id = deezer_.get_artist_id(chosen_artist)
  deezer_.get_album_list(id)
  genre = deezer_.pick_random()
  state = input("What is your state? ")
  state = state.replace(" ","+")
  '''
  This is what would've been used if events were found with the nearest city feature
  '''
  # loc = input("What is your location? ")
  # coordinates = m.coords_get(loc)
  # geo = GeoDB(coordinates)
  # nearest_city = geo.get_nearest_city()
  # seat.get_event_search(state,genre)
  seat.get_event_search(state,genre)
  chosen = int(input("Which number event interests you?"))
  print (seat.get_event(chosen))

main()
  