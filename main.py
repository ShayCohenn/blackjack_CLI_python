import random
from ascii_art import logo

start = input("Do you want to play a game of Blackjack? Type 'y' to start: ")

def deal_card():
  """returns a random card from the deck as an INT"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
  
def calculate_score(cards):
  """calculates the score of the cards in the list
  return 0 for win if the sum is 21 and if user got 11(A) swaps
  it to 1 and returns the sum of the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """compares the scores of the user and computer and returns
  a string of the result"""
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack"
  elif user_score == 0:
    return "Win with a Blackjack"
  elif user_score > 21:
    return "You went over. You lose"
  elif computer_score > 21:
    return "Opponent went over. You win"
  elif user_score > computer_score:
    return "You win"
  else:
    return "You lose"

def end_game(user_cards, computer_cards, user_score, computer_score):
  """end of game method - prints the final cards and score of both
  players and gives a choice to restart the game or not
  --- gets the user and computer cards, and user and computer scores as 
  inputs ---"""
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"The dealer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  play_again = input("Do you want to play again? Type 'y' to play again, type 'n' to exit: ")
  if play_again == "y":
    play_game()

def play_game():
  """main game function
  - prints the logo, initialize the user abd computer cards lists and 
  game over boolean
  - deals 2 cards to the user and computer
  - while the game is not over calcuates the scores and prints the
  cards.
  - if user or computer score is 21  or over end game 
  - if the game is not over ask the user if he wants to draw another card
  if not - end the game
  if yes - deal another card to the user and check if the game is over
  - if computer score is less than 17 drow another card for the computer
  - end the game/keep drowing cards"""
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}")
    print(f"The dealer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_game(user_cards, computer_cards, user_score, computer_score)
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        end_game(user_cards, computer_cards,user_score,computer_score)
        is_game_over = True

# Start the game if the user types 'y'
if start == 'y':
  play_game()