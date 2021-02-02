# Hangman(행맨) 미니 게임 제작
# 기본 프로그램 제작 및 테스트

import time
import random

# 처음 인사
name = input('What is your name? ')

print('Hi, ' + name + '. Have fun playing the Hangman game!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# 정답 단어
words = ['developer','secret','ant', 'balloon', 'book', 'cube', 'pencil', 'cup', 'coffee', 'tomorrow', 'yesterday', 'Cheetah', 'tiger', 'monster',
         'rabbit', 'December', 'music', 'guitar', 'keyboard', 'wonderwoman', 'devil', 'princess', 'kitty', 'glass', 'perfume', 'poison']  
w = random.choice(words) 


# 추측 단어
guesses = []

# 기회
turns = 10

# 그림 
HANGMAN_PICS = ['''
   
       
       
       
      ===''',
      '''
    
       |
       |
       |
      ===''','''
      --+
       |
       |
       |
      ===''','''
    +---+
       |
       |
       |
      ===''','''
    +---+
   O   |
       |
       |
      ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
       ===''','''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

# 찬스 카운트가 남아있을 경우
print('Let\'s guess the words.')
print()

while turns > 0:
    # 실패 횟수(문자 매치 수)
    failed = 0
    for char in w:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end=' ')
            failed += 1
    if failed == 0:
        print()
        print()
        print('Congratulations! The guesses are correct.')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input('Please enter a letter : ')

    # 같은 문자를 두번 입력했을 경우 
    print()
    guesses += guess
    if guess in guesses:
        print('The character has already been entered. Please enter another letter.')
              
    # 정답 단어에 추측한 문자가 포함되어 있지 않는 경우 
    if guess not in w:      
        turns -= 1
        # 오류 메시지
        print()
        print('Oops! wrong')
        # 남은 기회 출력
        print('You have', turns, 'more guesses!')
        if turns == 9:
            print(HANGMAN_PICS[0])
        elif turns == 8:
            print(HANGMAN_PICS[1])
        elif turns == 7:
            print(HANGMAN_PICS[2])
        elif turns == 6:
            print(HANGMAN_PICS[3])
        elif turns == 5:
            print(HANGMAN_PICS[4])
        elif turns == 4:
            print(HANGMAN_PICS[5])
        elif turns == 3:
            print(HANGMAN_PICS[6])
        elif turns == 2:
            print(HANGMAN_PICS[7])
        elif turns == 1:
            print(HANGMAN_PICS[8])             
        if turns == 0:
            # 실패 메시지
            print(HANGMAN_PICS[9])
            print('You failed. End the game. Bye!')


