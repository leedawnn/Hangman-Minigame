# Hangman(행맨) 미니 게임 제작

import time
import random
import csv
# import winsound

# 처음 인사
name = input('What is your name? ')

print('Hi, ' + name + '. Have fun playing the Hangman game!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# 랜덤 단어 
words = []

# 랜덤단어 csv 파일 로드
with open('/Users/leedawn/Documents/Hangman/Hangman-Minigame/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for c in reader:
        words.append(c)

random.shuffle(words)
q = random.choice(words)

# 정답 단어 
w = q[0].strip()

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
    # 문자 매치 수
    failed = 0

    for char in w:
        if char in guesses:
            print(char, end=' ')
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
    print('Hint: {}'.format(q[1].strip()))

    guess = input('Please enter a letter : ')

    print()
    # 문자 하나만 입력
    if len(guess) != 1:
        print('Please enter one English letter.')
        break

    # 같은 문자를 두번 입력했을 경우 
    if guess in guesses:
        print()
        print('The character has already been entered. Please enter another letter.')
    else:
        guesses += guess

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


