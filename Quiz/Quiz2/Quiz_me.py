import random

# 단어 리스트
words = ["apple", "banana", "orange"]

# 랜덤으로 단어 선택
word_to_guess = random.choice(words)

# 추측한 문자 저장할 집합
guessed_letters = set()

# 초기 상태 출력
current_state = ['_' if letter.isalpha() else letter for letter in word_to_guess]
print(" ".join(current_state))

# 기회 설정
max_attempts = 6
attempts_left = max_attempts

while attempts_left > 0:
    # 사용자로부터 문자 입력 받기
    guess = input("한 글자를 추측하세요: ").lower()

    # 이미 추측한 문자인지 확인
    if guess in guessed_letters:
        print("이미 추측한 글자입니다. 다시 시도하세요.")
        continue

    guessed_letters.add(guess)

    # 추측한 문자가 단어에 포함되는지 확인
    if guess in word_to_guess:
        print("정답입니다!")

        # 현재 상태 업데이트
        current_state = [char if char == guess or guessed.isalpha() else "_" for char, guessed in zip(word_to_guess, current_state)]

        # 현재 상태 출력
        print(" ".join(current_state))

        # 모든 글자를 맞추었을 경우 종료
        if "_" not in current_state:
            print("축하합니다! 정답을 맞추셨습니다.")
            break
    else:
        attempts_left -= 1
        print(f"틀렸습니다. 남은 기회: {attempts_left}")

        # 남은 기회가 없을 경우 종료
        if attempts_left == 0:
            print(f"게임 종료. 정답은 '{word_to_guess}'입니다.")
            break
