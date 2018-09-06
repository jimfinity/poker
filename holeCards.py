from card import card
class holeCards:
  veryStrongHands = [
                      [card('A','*'),card('A','*')], #Pair of Aces
                      [card('K','*'),card('K','*')], #Pair of Kings
                      [card('Q','*'),card('Q','*')], #Pair of Queens
                      [card('A','*'),card('K','*')], #Ace and King Suited and Unsuited
                    ]
  strongHands = [
                      [card('J','*'),card('J','*')], #Pair of Jacks
                      [card('10','*'),card('10','*')], #Pair of 10s
                      [card('9','*'),card('9','*')], #Pair of 9s
                      [card('A','*'),card('Q','*')], #Ace and Queen Suited and Unsuited
                      [card('A','C'),card('J','C')], #Ace and Jack Suited
                      [card('A','D'),card('J','D')], #^
                      [card('A','H'),card('J','H')], #^
                      [card('A','S'),card('J','S')], #^
                    ]

  def __init__(self, cards):
    if (len(cards) != 2):
      raise exception('they should only be 2 hole cards')
    else:
      self.cards = cards
      self.cards.sort()

  def preFlopAction(self,position,situation):
    if (self.cards in self.veryStrongHands):
      return 'Very Strong Hand'
    elif (self.cards in self.strongHands):
      return 'Strong Hand'
    else:
      return 'Fold'

  def __str__(self):
    return str(self.cards[0]) + ',' + str(self.cards[1])

pocket1 = holeCards(
                   [card('J','H'),card('A','D')]
                  )
pocket2 = holeCards(
                   [card('Q','H'),card('A','D')]
                  )
pocket3 = holeCards(
                   [card('A','H'),card('J','H')]
                  )

print (pocket1)
print (pocket1.preFlopAction('meh','meh'))
print (pocket2)
print (pocket2.preFlopAction('meh','meh'))
print (pocket3)
print (pocket3.preFlopAction('meh','meh'))
