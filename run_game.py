import requests
import time
from os import system
from bs4 import BeautifulSoup
from random import randrange

def game_choose_word():
    url = "https://www.ef-australia.com.au/english-resources/english-vocabulary/top-3000-words/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    words = soup.p.next_sibling.next_sibling
    num = randrange(0, 2999)
    word = words.find_all(string=True)[num][2:]
    return word

def play_game(word):
    win = 0
    lives = 9
    correct = []
    incorrect = []
    while (not win and lives > -1):
        lines = spell_word(word, correct, incorrect, lives)
        if (lines == 0):
            win = 1
            break

        guess = input("Enter a guess: ")
        system("cls")
        if len(guess) > 1 or not guess.isalpha():
            print("Your guess is invalid.\nYou must guess a letter.")
        elif guess.lower() in word:
            correct.append(guess[0].lower())
            print(guess, "was correct")
        else:
            incorrect.append(guess[0].lower())
            lives -= 1
    return win

def player_choose_word():
    word = input("Enter a word for the other player to guess: ")
    while not word.isalpha():
        word = input("Please enter a valid word: ")
    return word.lower()

def spell_word(word, correct, incorrect, lives):
    lines = 0
    for i in range(len(word)):
        if word[i] in set(correct):
            print(word[i], end = ' ')
        else:
            print('_', end = ' ')
            lines += 1

    if len(incorrect) > 0:
        print("\nIncorrect guesses: ")
        for i in range(len(incorrect)):
            print(incorrect[i], end = " ")

    print("\nYou have", lives, "lives left.")
    return lines