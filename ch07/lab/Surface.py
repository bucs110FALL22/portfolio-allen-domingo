import Rectangle

class Surface:
  def __init__(self,filename,x,y,h,w):
    '''
    Creates a screen for the drawing
    Args:
    filename - image filename for screen
    x - Starting x coordinate
    y - Starting y coordinate
    h - height of screen
    w - width of screen 
    No return
    '''
    self.rect = Rectangle.Rectangle(x,y,h,w)
    self.image = str(filename)
  def getRect(self):
    '''
    Returns the screen as a rectangle object
    '''
    return self.rect
    