class Rectangle:
  def __init__(self,x=0,y=0,h=0,w=0):
    '''
    Creates rectangle object
    Args:
    x - Starting x coordinate
    y - Starting y coordinate
    h - height of rectangle
    w - width of rectangle
    No Return
    '''
    if x < 0:
      x=0
    if y < 0:
      y=0
    if w < 0:
      w=0
    if h < 0:
      h=0    
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  def __str__(self):
    '''
    Returns a string statement highlighting details of rectangle (x,y and dimensions)

    '''
    return f"(x:{self.x_coord},y:{self.y_coord}) height:{self.height}, width:{self.width}"
