class Block:
  def __init__(self):
    self.coin_number = 1 #number of coins inside block 
    # self.coin_number = 1
    self.has_item = False
    self.emptied = False #if the block has no more coins or it does
    self.breakable = False #if the block can break
class Goomba:
  def __init__(self):
    self.alive = True #if the enemy is alive
    self.enemy_number = 12 #id number of enemy
    self.smooshed = False #if it displays as being 'smooshed'/if the goomba is killed
    self.place = (12,19) #position of enemy
    self.touching = False #if the Goomba is touching the player
class Item_Block:
  def __Init__(self):
    self.block_id = 8 #id of block
    self.emptied = False #if the block has its item or not
    self.item_inside = "Mushroom" #item within block