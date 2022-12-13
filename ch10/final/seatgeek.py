import requests

class SeatGeek:
  def __init__(self):
    '''
    initializes seatgeek class, stores urls and keys
    no args/returns
    '''
    self.api_key = "MzA4NTExNTF8MTY3MDQzMDE3My4yNjY4NjU"
    
    self.api_url = "https://api.seatgeek.com/2/events?genres[primary].slug="
    self.event_api_url = "https://api.seatgeek.com/2/events/"
  def get_event_search(self,location,genre):
    '''
   searches for event
   args:
   location: state given by user
   genre: genre of artist looked up
   returns - none, just prints a list of events for the user to choose
    '''
   
    self.request = requests.request("GET",f"{self.api_url}{genre}&q={location}&client_id={self.api_key}").json()
    self.event_list = []
    # print(request)
    if self.request["events"]:
      number = 1 
      print("Here's a list of events:")
      for event in self.request["events"]:
        print(f"{number})",event["title"],'in', event["venue"]['city'])
        self.event_list.append(event['id'])
        number += 1
        
    else:
      print("no events found")
  def get_event(self,event_num):
    '''
    gives the user a link to buy tickets based on the chose n event
    args:
    event_num: event chosen
    returns the link for the user to get tickets
    '''
    # event_id = self.event_list[event_num-1]
    
    end_message = "Here's a link to buy tickets to the event!:",self.request["events"][event_num-1]['url']
    return end_message
    # print(event_request)

    