# Hangman-Minigame

## 게임설명

컴퓨터가 내는 단어를 맞춰야한다. 알파벳 중 한 글자만 입력한다. <br>
입력한 글자가 정답 단어 안에 있을 경우 글자를 출력하고, 정답이 아닐 시 기회를 하나씩 깎는다. 


총 기회 횟수는 10번이며, 기회가 깎일 때마다 '교수대-밧줄-머리-팔-손-몸통-다리-발' 순서로 그림이 출력된다. 기회가 모두 소진되면 게임이 종료된다.

```python
if failed == 0:
    print('Congratulations! The guesses are correct.')
    break
```