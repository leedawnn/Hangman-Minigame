# Hangman(행맨) 미니 게임 제작
# 기본 프로그램 제작 및 테스트

import time

# 처음 인사
name = input('What is your name?')

print('Hi, ' + name + 'Have fun playing the Hangman game!')

print()

time.sleep(1)

print('Start Loading...')
print()
time.sleep(0.5)

# 정답 단어
word = 'secret'

# 추측 단어
guesses = ''

# 기회
turns = 10

# 찬스 카운트가 남아있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1
        if failed == 0:
            print()
            print()
            print('Congratulations! The guesses are correct.')
            break
        print()

        # 추측 단어 문자 단위 입력
        print()
        guess = input('Guess a character.')

        guess += guess

        # 정답 단어에 추측한 문자가 포함되어 있지 않는 경우 
        if guess not in word:      
            turns -= 1
            # 오류 메시지
            print('Oops! wrong') 
            # 남은 기회 출력
            print('You have', turns, 'more guesses!')

            if turns == 0:
                # 실패 메시지
                print('You failed. End the game. Bye!')



