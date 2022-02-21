import random
import art
import replit

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_card(dec, num):
  for i in range(len(dec)):
    if dec[i] == num:
      return True
  
def add_to_cdeck(udeck):
  d = len(udeck)-1
  while d > 0:
    c_deck.append(random.choice(cards))
    d -= 1

def check_winner(deck,c_deck):
   
  print(f"Your final cards: {deck}, final score: {sum(deck)}")
  print(f"The computer's final cards are: {c_deck}, final score: {sum(c_deck)}")
  if sum(deck) > 21:
    print("You lose")
  elif sum(deck) > sum(c_deck):
    print("You Win!!!")
  elif sum(deck) == sum(c_deck):
    print("A Draw!")
  elif sum(deck) < sum(c_deck):
    if sum(c_deck) > 21:
      print("You win")
    else:
      print("You LOOOse")

print(art.logo)
print("Hello, welcome to Blackjack \n")


stop = False
while not stop:
  okay = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
  
  if okay == "y":
    replit.clear()

    print(art.logo)
    print("Hello, welcome to Blackjack \n")

    deck = [random.choice(cards), random.choice(cards)]
    c_deck = [random.choice(cards)]
    
    print(f"Your cards: {deck}, current score {sum(deck)}")
    print(f"The computer's first card is: {c_deck}")
    sec_stop = True
    while sec_stop :
      con = input("Type 'y' to add a new card, or type 'n' to pass: ").lower()
      if con == 'y':
        deck.append(random.choice(cards))
        print(f"Your cards: {deck}, current score {sum(deck)}")
        print(f"The computer's card: {c_deck} \n")
        if sum(deck) > 21 and ace_card(deck, 11 ) == True:
          # if your sum is above 21 and you havve an ace 
          # print("yello")
          sumdeck = sum(deck)
          sumdeck -= 10
          p = deck.index(11)
          deck.insert(p, 1 )
          add_to_cdeck(deck)
          
          check_winner(deck,c_deck)
          sec_stop = False
        elif sum(deck) > 21:
          add_to_cdeck(deck)
          check_winner(deck, c_deck)
          sec_stop = False
      elif con == 'n':
        # print("'you typed 'n'")
        add_to_cdeck(deck)
        
        check_winner(deck,c_deck)
        sec_stop = False
      else:
        sec_stop = False
        
  else:
    print("Okay, Bye")
    stop = True
  # print(sum_deck)
