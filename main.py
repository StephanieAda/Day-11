import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def user_cards():
  deck = [random.choice(cards), random.choice(cards)]
  
def com_cards():
  c_deck = random.choice(cards)
  return c_deck
user_cards()

print("Hello, welcome to Blackjack")

deck = [random.choice(cards), random.choice(cards)]
c_deck = [random.choice(cards)]
print("Do you want to play a game of blackjack? Type 'y' or 'n'")
print(f"Your cards: {deck}, current score {sum(deck)}")
print(f"The computer's first card is: {c_deck}")
while sum(deck) < 21 :
  con = input("Type 'y' to add a new card, or type 'n' to stand: ").lower()
  if con == 'y':
    deck.append(random.choice(cards))
    
    print(f"Your cards: {deck}, current score {sum(deck)}")
    if sum(deck) > 21:
      print("you lose")
  else: