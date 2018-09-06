class card:
  values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
  #The * suit is used for wildcard matching
  suits = ('S','C','D','H','*')

  def __init__(self, value, suit):
    if value not in  self.values:
       raise Exception('Not a Valid card value')
    if suit not in self.suits:
        raise Exception('Not a valid card suit')
    self.value = value
    self.suit = suit

  def __str__(self):
    stringRep = 'The ' + self.value + ' of ' + self.getSuit()
    return stringRep

  def __gt__(self, secondCard):
    #if(self.values.index(self.getValue()) > self.values.index(secondCard.getValue())):
    if(self.getValueNum() > secondCard.getValueNum()):
      return True
    elif (self.getValueNum() == secondCard.getValueNum()):
      return self.getSuit() > secondCard.getSuit()
    else:
      return False

  def __lt__(self, secondCard):
    #if(self.values.index(self.getValue()) < self.values.index(secondCard.getValue())):
    if(self.getValueNum() > secondCard.getValueNum()):
      return True
    elif (self.getValueNum() == secondCard.getValueNum()):
      return self.getSuit() > secondCard.getSuit()
    else:
      return False

  def __eq__(self, secondCard):
#    if(
#        (self.getValueNum() == secondCard.getValueNum())
#          and
#          (
#            self.getSuit() == secondCard.getSuit()
#              or
#              (
#                self.getSuit() == '*' or secondCard.getSuit == '*'
#              )
#          )
#      ):
    if((self.getValueNum() == secondCard.getValueNum())):
      return True
    return False

  def getValue(self):
    if (self.value == 'A'):
      return 'Ace'
    elif (self.value == 'K'):
      return 'King'
    elif (self.value == 'Q'):
      return 'Queen'
    elif (self.value == 'J'):
      return 'Jack'
    else:
      return self.value

  def getValueNum(self):
    if (self.value == 'A'):
      return 14
    elif (self.value == 'K'):
      return 13
    elif (self.value == 'Q'):
      return 12
    elif (self.value == 'J'):
      return 11
    else:
      return int(self.value)

  def getSuit(self):
    suit_string = {
                 'S':'Spades',
                 'C':'Clubs',
                 'D':'Diamonds',
                 'H':'Hearts'
                }
    return suit_string[self.suit]

  def matchesSuit(self,secondCard):
    if(self.getSuit() == secondCard.getSuit()):
      return True
    return False

  def plusOne(self):
    #this should return the next card, needed for straight calculation
    return card('A','S')
