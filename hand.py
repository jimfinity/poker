from card import card
class hand:
  ranking_hands = {
  'Straight Flush':9,
  'Four of a Kind':8,
  'Full House':7,
  'Flush':6,
  'Straight':5,
  'Three of a Kind':4,
  'Two Pair':3,
  'Pair':2,
  'High Card':1,
  }

  def __init__(self,cards):
    if (len(cards) != 5):
      raise Exception('Not a valid hand')
    #return self.rank(cards)
    self.rank = self.rank(cards)
    #print (self)

  def rank(self,cards):
    #sorts the list into numerical order
    cards.sort()
    sorted_cards = cards.copy()
#    for c in sorted_cards:
#      print (c)
    #list used to stored card values numerically for easier comparison
    card_values = []
    #list used to stored cards suits to check for flushes
    card_suits = []
    #for each card in the hand get the value and suit
    for j in sorted_cards:
      #stored the suit
      card_suits.append(j.getSuit())
      #store the int value of the card
      card_values.append(int(j.getValueNum()))
    #check if the cards values are consecutive (a straight)
    if (
        (card_values[1] == (card_values[0] + 1)
          and
          card_values[2] == (card_values[1] + 1)
          and
          card_values[3] == (card_values[2] + 1)
          and
          card_values[4] == (card_values[3] + 1) )
        #the or statement expresses a 5 high straight manually
        or
        (card_values[0] == 2
         and
         card_values[1] == 3
         and
         card_values[2] == 4
         and
         card_values[3] == 5
         and
         card_values[4] == 14
         )
       ):
      #if there is a straight check for a straight flush
      if (
          card_suits[1] == card_suits[0]
          and
          card_suits[2] == card_suits[1]
          and
          card_suits[3] == card_suits[2]
          and
          card_suits[4] == card_suits[3]
         ):
        #return 'Straight Flush of ' + card_suits[0] + ' ' + sorted_cards[4].getValue() + ' high'
        if (card_values[3] == 5 and card_values[4] == 14):
          high_card = cards[3]
        else:
          high_card = cards[4]
        return {'rank':'Straight Flush',
                'details':{'high_card':high_card.getValue(),
                           'value':high_card.getValueNum(),
                           'suit':card_suits[0],
                           'cards':cards}
               }
      #return 'Straight ' + sorted_cards[4].getValue() + ' high'
      if (card_values[3] == 5 and card_values[4] == 14):
        high_card = cards[3]
      else:
        high_card = cards[4]
      return {'rank':'Straight',
              'details':{'high_card':high_card.getValue(),
                         'value':high_card.getValueNum(),
                         'cards':cards}
               }
    #if no straight then check for a flush
    elif(
          card_suits[1] == card_suits[0]
          and
          card_suits[2] == card_suits[1]
          and
          card_suits[3] == card_suits[2]
          and
          card_suits[4] == card_suits[3]
         ):
      #return 'Flush ' + sorted_cards[4].getValue() + ' high'
      return {'rank':'Flush',
              'details':{'high_card':sorted_cards[4].getValue(),
                       'value':sorted_cards[4].getValueNum(),
                       'suit':card_suits[0],
                       'cards':cards}
               }
    #check cards for duplicates
    for i in sorted_cards:
      #remove the card (i) from the list so it doesn't match
      sorted_cards.remove(i)
      #check for 1 match (pair)
      if i in sorted_cards:
        sorted_cards.remove(i)
        #check for 2 matches (three of a kind)
        if i in sorted_cards:
          sorted_cards.remove(i)
          #check for 3 matches (4 of a kind)
          if i in sorted_cards:
            #return 'Four of a kind'
            return {'rank':'Four of a Kind',
                    'details':{'value':i.getValueNum(),
                               'quad':i.getValue(),
                               'cards':cards}
                   }
          #if 2 matches are made, check if the remaining 2 cards are a pair
          elif (len(sorted_cards) == 2):
            if (sorted_cards[0] == sorted_cards[1]):
              #return 'Full House'
              return {'rank':'Full House',
                      'details':{'triple':cards[0].getValue(),
                                 'pair':sorted_cards[0].getValue(),
                                 'value':[cards[0].getValueNum(),cards[4].getValueNum()],
                                 'cards':cards}
                     }
          #return 'Three of a kind'
          return {'rank': 'Three of a Kind',
                  'details': {'value':i.getValueNum(),
                              'triple':i.getValue(),
                              'cards':cards}
                 }
        #if there is a pair but not 3 of that match check the other 3 cards
        #for a full house or two pairs
        elif (len(sorted_cards) == 3):
          if (sorted_cards[0] == sorted_cards[1] and sorted_cards[1] == sorted_cards[2]):
            #return 'Full House'
            return {'rank':'Full House',
                    'details':{'triple':sorted_cards[0].getValue(),
                               'pair':cards[0].getValue(),
                               'value':[cards[0].getValueNum(),cards[4].getValueNum()],
                               'cards':cards}
                   }
          elif (sorted_cards[0] == sorted_cards[1] or sorted_cards[1] == sorted_cards[2]):
            #return 'Two Pair'
            return {'rank':'Two Pair',
                    'details':{'value':[card_values[1],card_values[3]],
                               'pairs':[cards[1].getValue(),cards[3].getValue()],
                               'cards':cards}
                   }
          else:
            break

        elif (len(sorted_cards) == 2):
          if (sorted_cards[0] == sorted_cards[1]):
            #return 'Two Pair'
            return {'rank':'Two Pair',
                    'details':{'value':[card_values[1],card_values[3]],
                               'pairs':[cards[1].getValue(),cards[3].getValue()],
                               'cards':cards}
                   }
        else:
          #return 'Pair of '+ i.getValue() +  's'
          return {'rank':'Pair',
                  'details':{'pair':i.getValue(),
                             'value':i.getValueNum(),
                             'cards':cards}
                 }
    #return 'trash'
    return {'rank':'High Card',
            'details':{'high_card':cards[4].getValue(),
                     'value':card_values[4],
                     'cards':cards}
           }

  def __str__(self):
    if (self.rank['rank'] == 'Straight Flush'):
      return self.rank['rank'] + ' ' + self.rank['details']['suit'] + ' ' + self.rank['details']['high_card'] + ' high'
    if (self.rank['rank'] == 'Four of a Kind'):
      return self.rank['rank'] + ' ' + self.rank['details']['quad'] + 's'
    if (self.rank['rank'] == 'Full House'):
      return self.rank['rank'] + ' ' + self.rank['details']['triple'] + 's full of ' + self.rank['details']['pair'] + 's'
    if (self.rank['rank'] == 'Flush'):
      return self.rank['rank'] + ' ' + self.rank['details']['suit'] + ' ' + self.rank['details']['high_card'] + ' high'
    if (self.rank['rank'] == 'Straight'):
      return self.rank['rank'] + ' ' + self.rank['details']['high_card'] + ' high'
    if (self.rank['rank'] == 'Three of a Kind'):
      return self.rank['rank'] + ' ' + self.rank['details']['triple'] + 's'
    if (self.rank['rank'] == 'Two Pair'):
      return self.rank['rank'] + ' ' + self.rank['details']['pairs'][1] + 's and ' + self.rank['details']['pairs'][0] + 's'
    if (self.rank['rank'] == 'Pair'):
      return self.rank['rank'] + ' of ' + self.rank['details']['pair'] + 's'
    if (self.rank['rank'] == 'High Card'):
      return self.rank['rank'] + ' - ' + self.rank['details']['high_card'] + ' high'
    else:
      return self.rank['rank'] + ' ' + str(self.rank['details']['value'])

  def __gt__(self,hand):
    if (self.ranking_hands[self.getRank()] != self.ranking_hands[hand.getRank()]):
      return self.ranking_hands[self.getRank()] > self.ranking_hands[hand.getRank()]
    elif (self.getRank() == 'Straight Flush'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] > second_hand['details']['value']
    elif (self.getRank() == 'Straight'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] > second_hand['details']['value']
    else:
      return self.ranking_hands[self.getRank()] > self.ranking_hands[hand.getRank()]
    #return false

  def __lt__(self,hand):
    if (self.ranking_hands[self.getRank()] != self.ranking_hands[hand.getRank()]):
      return self.ranking_hands[self.getRank()] < self.ranking_hands[hand.getRank()]
    elif (self.getRank() == 'Straight Flush'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] < second_hand['details']['value']
    elif (self.getRank() == 'Straight'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] < second_hand['details']['value']
    else:
      return self.ranking_hands[self.getRank()] < self.ranking_hands[hand.getRank()]
    #return true

  def __eq__(self,hand):
    if (self.ranking_hands[self.getRank()] != self.ranking_hands[hand.getRank()]):
      return False
    elif (self.getRank() == 'Straight Flush'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] == second_hand['details']['value']
    elif (self.getRank() == 'Straight'):
      first_hand = self.getFullRank()
      second_hand = hand.getFullRank()
      return first_hand['details']['value'] == second_hand['details']['value']
    else:
      return self.ranking_hands[self.getRank()] < self.ranking_hands[hand.getRank()]
    #return self.ranking_hands[self.getRank()] == self.ranking_hands[hand.getRank()]
    #return true

  def getRank(self):
    return self.rank['rank']

  def getFullRank(self):
    return self.rank

'''
print('3D,AD,5D,7S,JC - High Card Ace')
hand([card('3','D'),card('A','D'),card('5','D'),card('7','S'),card('J','C')])

print('3D,AD,5D,7S,3C - Pair of 3s')
hand([card('3','D'),card('A','D'),card('5','D'),card('7','S'),card('3','C')])

print('2D,2C,5D,7S,2H - Three of a kind')
hand([card('2','D'),card('2','C'),card('5','D'),card('7','S'),card('2','H')])

print('2D,5C,5D,7S,5H - Three of a kind')
hand([card('2','D'),card('5','C'),card('5','D'),card('7','S'),card('5','H')])

print('3D,3H,3S,7S,3C - Four of a kind')
hand([card('3','D'),card('3','H'),card('3','S'),card('7','S'),card('3','C')])

print('AD,AH,AS,7S,AC - Four of a kind')
hand([card('A','D'),card('A','H'),card('A','S'),card('7','S'),card('A','C')])

print('2D,2C,5D,5S,2H - Full House (3 lower than the pair)')
hand([card('2','D'),card('2','C'),card('5','D'),card('5','S'),card('2','H')])

print('2D,5C,5D,5S,2H - Full House (3 higher than the pair)')
hand([card('2','D'),card('5','C'),card('5','D'),card('5','S'),card('2','H')])

print('2D,5C,AD,4S,3H - Straight 5 High')
hand([card('2','D'),card('5','C'),card('A','D'),card('4','S'),card('3','H')])

print('4D,5C,6D,7S,8H - Straight 8 High')
hand([card('4','D'),card('5','C'),card('6','D'),card('7','S'),card('8','H')])

print('AD,10C,JD,QS,KH - Straight Ace high')
hand([card('A','D'),card('10','C'),card('J','D'),card('Q','S'),card('K','H')])

print('AD,2D,3D,4D,5D - Straight Flush Diamonds 5 High')
hand([card('A','D'),card('2','D'),card('3','D'),card('4','D'),card('5','D')])

print('9D,10D,JD,QD,KD - Straight Flush Diamonds King High')
hand([card('9','D'),card('10','D'),card('J','D'),card('Q','D'),card('K','D')])

print('AD,10D,JD,QD,KD - Straight Flush Diamonds Ace High')
hand([card('A','D'),card('10','D'),card('J','D'),card('Q','D'),card('K','D')])

print('9D,10D,4D,QD,KD - Flush King High')
hand([card('9','D'),card('10','D'),card('4','D'),card('Q','D'),card('K','D')])

print('3D,AD,5D,7S,AC - Pair')
hand([card('3','D'),card('A','D'),card('5','D'),card('7','S'),card('A','C')])

print('3D,AD,5D,5S,AC - Two Pair ABBCC')
hand([card('3','D'),card('A','D'),card('5','D'),card('5','S'),card('A','C')])

print('3D,AD,3D,5S,AC - Two Pair AABCC')
hand([card('3','D'),card('A','D'),card('3','D'),card('5','S'),card('A','C')])

print('3D,AD,5D,5S,3C - Two Pair AABBC')
hand([card('3','D'),card('A','D'),card('5','D'),card('5','S'),card('3','C')])
'''

list_of_hands = [
hand([card('9','D'),card('10','D'),card('4','D'),card('Q','D'),card('K','D')]),
hand([card('A','D'),card('2','D'),card('3','D'),card('4','D'),card('5','D')]),
hand([card('A','D'),card('A','H'),card('A','S'),card('7','S'),card('A','C')]),
hand([card('3','D'),card('A','D'),card('5','D'),card('7','S'),card('A','C')]),
hand([card('3','D'),card('A','D'),card('3','D'),card('5','S'),card('A','C')]),
hand([card('A','D'),card('10','C'),card('J','D'),card('Q','S'),card('K','H')]),
hand([card('9','D'),card('10','C'),card('J','D'),card('Q','S'),card('K','H')]),
hand([card('2','D'),card('5','C'),card('A','D'),card('4','S'),card('3','H')]),
hand([card('9','D'),card('10','D'),card('J','D'),card('Q','D'),card('K','D')]),
hand([card('A','D'),card('10','D'),card('J','D'),card('Q','D'),card('K','D')]),
hand([card('A','D'),card('A','S'),card('A','C'),card('Q','D'),card('A','H')])
]

list_of_hands.sort()
list_of_hands.reverse()
i=1
for each_hand in list_of_hands:
  print (i)
  print(each_hand)
  i=i+1
