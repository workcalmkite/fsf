import streamlit as st
import random
import time

st.set_page_config(page_title="3분마다 랜덤 게임", page_icon="🎮")

# 게임 목록 정의
games = [
    "숫자 맞추기", "퀴즈", "틱택토", "가위바위보",
    "단어 뒤집기", "카운트다운 클릭", "맞춤형 선택 게임",
    "숨은 단어 찾기", "계산 게임", "기억력 게임",
    "타이핑 게임", "랜덤 이야기 만들기"
]

# 게임 선택
if "last_game_time" not in st.session_state:
    st.session_state.last_game_time = 0
    st.session_state.current_game = random.choice(games)

current_time = time.time()

# 3분마다 게임 변경
if current_time - st.session_state.last_game_time > 180:
    st.session_state.current_game = random.choice(games)
    st.session_state.last_game_time = current_time

st.title("🎮 3분마다 랜덤 게임 🎮")
st.subheader(f"현재 게임: {st.session_state.current_game}")

# 간단한 게임 구현
def number_guess_game():
    st.write("1부터 10 사이의 숫자를 맞춰보세요!")
    number = random.randint(1, 10)
    guess = st.number_input("숫자를 입력하세요", min_value=1, max_value=10, step=1)
    if st.button("확인"):
        if guess == number:
            st.success("🎉 맞췄어요!")
        else:
            st.error(f"아쉽네요! 정답은 {number}였습니다.")

def simple_quiz():
    question = "파이썬의 로고 색은?"
    options = ["빨강", "파랑-노랑", "초록", "검정"]
    answer = "파랑-노랑"
    choice = st.radio(question, options)
    if st.button("제출"):
        if choice == answer:
            st.success("정답!")
        else:
            st.error(f"오답! 정답은 {answer}입니다.")

# 게임 실행
if st.session_state.current_game == "숫자 맞추기":
    number_guess_game()
elif st.session_state.current_game == "퀴즈":
    simple_quiz()
else:
    st.info("이 게임은 아직 준비 중입니다. 곧 추가됩니다!")

# 남은 시간 표시
remaining = max(0, 180 - int(current_time - st.session_state.last_game_time))
minutes = remaining // 60
seconds = remaining % 60
st.write(f"다음 게임까지: {minutes:02d}:{seconds:02d}")
