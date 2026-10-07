import streamlit as st
import time

# ============================================================
# 기본 설정
# ============================================================

st.set_page_config(
    page_title="폐교의 마지막 교실",
    page_icon="🏫",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS - 쯔꾸르풍 UI
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&family=Noto+Sans+KR:wght@400;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 50% 20%, #303030 0%, #151515 45%, #090909 100%);
    color: #eeeeee;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

.game-title {
    font-family: 'Black Han Sans', sans-serif;
    text-align: center;
    font-size: 42px;
    color: #e8d7a5;
    text-shadow: 3px 3px 0px #000;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #999;
    margin-bottom: 25px;
}

.room {
    position: relative;
    height: 360px;
    border: 8px solid #262626;
    border-radius: 5px;
    overflow: hidden;
    background:
        linear-gradient(
            rgba(30,30,30,0.15),
            rgba(0,0,0,0.45)
        ),
        repeating-linear-gradient(
            90deg,
            #584f45 0px,
            #584f45 70px,
            #4e463e 72px,
            #4e463e 140px
        );
    box-shadow:
        inset 0 0 80px rgba(0,0,0,0.8),
        0 10px 30px rgba(0,0,0,0.6);
}

.floor {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 95px;
    background:
        repeating-linear-gradient(
            0deg,
            #392f29 0px,
            #392f29 18px,
            #2b2420 20px,
            #2b2420 38px
        );
    border-top: 5px solid #171717;
}

.window {
    position: absolute;
    left: 55px;
    top: 45px;
    width: 150px;
    height: 150px;
    background:
        radial-gradient(circle at 50% 40%, #38495c, #111923 75%);
    border: 10px solid #292929;
    box-shadow: inset 0 0 30px #000;
}

.window::before {
    content: "";
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 7px;
    background: #252525;
}

.window::after {
    content: "";
    position: absolute;
    left: 0;
    right: 0;
    top: 50%;
    height: 7px;
    background: #252525;
}

.clock {
    position: absolute;
    right: 65px;
    top: 35px;
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: #d8d1bd;
    border: 6px solid #272727;
    color: #111;
    text-align: center;
    padding-top: 21px;
    font-weight: 900;
}

.door {
    position: absolute;
    right: 65px;
    bottom: 45px;
    width: 90px;
    height: 175px;
    background: linear-gradient(90deg, #392318, #5b3622, #3b2419);
    border: 7px solid #24170f;
    box-shadow: inset 0 0 25px #111;
}

.door-handle {
    position: absolute;
    right: 12px;
    top: 95px;
    width: 13px;
    height: 13px;
    background: #d1a84e;
    border-radius: 50%;
}

.desk {
    position: absolute;
    left: 280px;
    bottom: 80px;
    width: 150px;
    height: 75px;
    background: #4b3020;
    border: 5px solid #291a12;
    box-shadow: 0 10px 0 #24170f;
}

.desk::before,
.desk::after {
    content: "";
    position: absolute;
    bottom: -50px;
    width: 15px;
    height: 50px;
    background: #2a1a12;
}

.desk::before {
    left: 10px;
}

.desk::after {
    right: 10px;
}

.board {
    position: absolute;
    left: 280px;
    top: 30px;
    width: 180px;
    height: 90px;
    background: #18251d;
    border: 8px solid #39291e;
    color: #aebba8;
    padding: 15px;
    font-family: monospace;
    font-size: 14px;
}

.player {
    position: absolute;
    left: 210px;
    bottom: 65px;
    font-size: 48px;
    filter: drop-shadow(3px 5px 2px #000);
}

.safe {
    position: absolute;
    left: 485px;
    bottom: 92px;
    font-size: 55px;
    filter: drop-shadow(3px 4px 2px #000);
}

.dark-overlay {
    position: absolute;
    inset: 0;
    background: radial-gradient(
        circle,
        transparent 20%,
        rgba(0,0,0,0.65) 80%
    );
    pointer-events: none;
}

.dialogue {
    background: #101010;
    border: 3px solid #777;
    border-radius: 5px;
    padding: 18px;
    margin: 15px 0;
    box-shadow: 0 5px 15px #000;
}

.dialogue-name {
    color: #e5c36a;
    font-weight: 900;
    margin-bottom: 8px;
}

.inventory {
    background: #111;
    border: 2px solid #555;
    padding: 12px;
    border-radius: 5px;
}

.inventory-title {
    color: #e5c36a;
    font-weight: bold;
}

.item {
    display: inline-block;
    background: #292929;
    border: 1px solid #777;
    padding: 5px 10px;
    margin: 3px;
    border-radius: 3px;
}

.warning-box {
    background: #301717;
    border: 2px solid #8d4141;
    padding: 12px;
    border-radius: 5px;
    color: #ffb0b0;
}

.success-box {
    background: #142a1a;
    border: 2px solid #4e9a60;
    padding: 15px;
    border-radius: 5px;
    color: #b7ffc3;
}

.hint-box {
    background: #272514;
    border: 2px solid #80783c;
    padding: 12px;
    border-radius: 5px;
    color: #eee1a0;
}

.timer {
    text-align: center;
    font-size: 22px;
    color: #d86b6b;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    background: #292929;
    color: #eee;
    border: 2px solid #555;
    border-radius: 4px;
    min-height: 45px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #3e3e3e;
    border-color: #c6a95b;
    color: #fff;
}

div[data-testid="stTextInput"] input {
    background: #111;
    color: #fff;
    border: 2px solid #555;
}

hr {
    border-color: #444;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 게임 초기화
# ============================================================

def reset_game():
    st.session_state.started = True
    st.session_state.start_time = time.time()

    st.session_state.drawer_open = False
    st.session_state.key_found = False

    st.session_state.board_checked = False
    st.session_state.clue_found = False

    st.session_state.safe_checked = False
    st.session_state.safe_open = False

    st.session_state.code = ""
    st.session_state.door_checked = False

    st.session_state.escaped = False
    st.session_state.game_over = False

    st.session_state.message = (
        "눈을 떠보니 오래된 교실이다. "
        "문은 잠겨 있고 창문은 굳게 닫혀 있다."
    )


if "started" not in st.session_state:
    st.session_state.started = False


# ============================================================
# 시작 화면
# ============================================================

if not st.session_state.started:

    st.markdown(
        '<div class="game-title">폐교의 마지막 교실</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">3분 안에 교실을 탈출하라</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="dialogue">
        <div class="dialogue-name">???</div>
        <div>
        삐걱…….<br><br>
        오래된 형광등이 깜빡인다.<br>
        정신을 차려보니 당신은 아무도 없는 폐교의 교실에 갇혀 있다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hint-box">
    🎯 <b>목표</b><br>
    교실을 조사하고 단서를 찾아 잠긴 문을 열어라.<br>
    제한 시간은 <b>3분</b>이다.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("▶ 게임 시작", use_container_width=True):
        reset_game()
        st.rerun()

    st.caption("※ 모바일에서도 플레이할 수 있습니다.")

    st.stop()


# ============================================================
# 게임 종료
# ============================================================

if st.session_state.escaped:

    st.balloons()

    st.markdown(
        '<div class="game-title">탈출 성공</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="success-box">
        <h2>🚪 문이 열렸다.</h2>
        <p>
        차가운 복도가 눈앞에 펼쳐진다.<br><br>
        당신은 마지막 교실에서 무사히 탈출했다.
        </p>
        <hr>
        <b>END</b>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("🔄 다시 플레이"):
        reset_game()
        st.rerun()

    st.stop()


# ============================================================
# 제한시간
# ============================================================

elapsed = int(time.time() - st.session_state.start_time)
remaining = max(0, 180 - elapsed)

minutes = remaining // 60
seconds = remaining % 60

st.markdown(
    f'<div class="timer">⏱ 남은 시간 {minutes:02d}:{seconds:02d}</div>',
    unsafe_allow_html=True
)

if remaining <= 0:

    st.session_state.game_over = True

    st.markdown("""
    <div class="warning-box">
        <h2>💀 시간이 다 되었다.</h2>
        교실의 불이 꺼졌다.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 다시 시작"):
        reset_game()
        st.rerun()

    st.stop()


# ============================================================
# 제목
# ============================================================

st.markdown(
    '<div class="game-title">폐교의 마지막 교실</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Chapter 1 — 마지막 수업</div>',
    unsafe_allow_html=True
)


# ============================================================
# 교실 화면
# ============================================================

st.markdown("""
<div class="room">

    <div class="window"></div>

    <div class="clock">11:47</div>

    <div class="board">
        TODAY<br>
        수학 시험<br><br>
        "답은 거꾸로 보아라."
    </div>

    <div class="desk"></div>

    <div class="safe">🔐</div>

    <div class="door">
        <div class="door-handle"></div>
    </div>

    <div class="player">🧍</div>

    <div class="floor"></div>

    <div class="dark-overlay"></div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# 현재 상황
# ============================================================

st.markdown(
    f"""
    <div class="dialogue">
        <div class="dialogue-name">나</div>
        {st.session_state.message}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# 인벤토리
# ============================================================

items = []

if st.session_state.key_found:
    items.append("🗝️ 낡은 열쇠")

if st.session_state.clue_found:
    items.append("📜 숫자 단서")

if st.session_state.safe_open:
    items.append("🔐 금고 내용물")

if items:
    item_html = "".join(
        f'<span class="item">{item}</span>'
        for item in items
    )

    st.markdown(
        f"""
        <div class="inventory">
            <div class="inventory-title">🎒 소지품</div>
            {item_html}
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown("""
    <div class="inventory">
        <div class="inventory-title">🎒 소지품</div>
        비어 있음
    </div>
    """, unsafe_allow_html=True)


st.write("")


# ============================================================
# 행동 버튼
# ============================================================

st.subheader("🔎 조사하기")

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# 서랍
# ------------------------------------------------------------

with col1:

    if st.button("🗄️ 교탁 서랍 조사"):

        if not st.session_state.drawer_open:

            st.session_state.drawer_open = True
            st.session_state.key_found = True

            st.session_state.message = (
                "서랍 안에는 먼지가 가득하다. "
                "손을 넣어보니 차가운 금속이 만져진다. "
                "🗝️ 낡은 열쇠를 얻었다."
            )

        else:

            st.session_state.message = (
                "서랍은 이미 열어봤다. "
                "더 이상 특별한 것은 없다."
            )

        st.rerun()


# ------------------------------------------------------------
# 칠판
# ------------------------------------------------------------

with col2:

    if st.button("🧑‍🏫 칠판 조사"):

        if not st.session_state.board_checked:

            st.session_state.board_checked = True
            st.session_state.clue_found = True

            st.session_state.message = (
                "칠판 구석에 희미하게 적힌 문장이 있다.\n\n"
                "『답은 거꾸로 보아라.』\n\n"
                "그리고 아래에 숫자가 적혀 있다."
            )

        else:

            st.session_state.message = (
                "칠판에는 여전히 같은 문장이 보인다.\n"
                "『답은 거꾸로 보아라.』"
            )

        st.rerun()


# ------------------------------------------------------------
# 금고
# ------------------------------------------------------------

if st.button("🔐 책장 아래의 금고 조사"):

    if not st.session_state.key_found:

        st.session_state.message = (
            "작은 금고가 있다. "
            "열쇠 구멍이 보인다."
        )

    elif not st.session_state.safe_open:

        st.session_state.safe_checked = True

        st.session_state.message = (
            "낡은 열쇠를 금고에 넣었다.\n"
            "찰칵.\n\n"
            "금고가 열렸다."
        )

        st.session_state.safe_open = True

    else:

        st.session_state.message = (
            "금고는 이미 열려 있다.\n"
            "안쪽에 숫자 2684가 적힌 종이가 있다."
        )

    st.rerun()


# ============================================================
# 금고 내용
# ============================================================

if st.session_state.safe_open:

    st.markdown("""
    <div class="hint-box">
        📜 금고 안에서 종이를 발견했다.<br><br>
        <b>2684</b><br><br>
        하지만 칠판에는 "답은 거꾸로 보아라"라고 적혀 있었다.
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("🔢 문 비밀번호")

    code = st.text_input(
        "비밀번호 4자리를 입력하세요.",
        max_chars=4,
        placeholder="예: 1234",
        key="password_input"
    )

    if st.button("🔓 비밀번호 확인"):

        # 2684를 거꾸로 읽으면 4862
        if code == "4862":

            st.session_state.door_checked = True
            st.session_state.escaped = True

            st.session_state.message = (
                "철컥…….\n\n"
                "문이 열렸다."
            )

            st.rerun()

        else:

            st.session_state.message = (
                "삐빅.\n\n"
                "비밀번호가 틀렸다."
            )

            st.rerun()


# ============================================================
# 문 조사
# ============================================================

st.write("")

if st.button("🚪 교실 문 조사"):

    if not st.session_state.safe_open:

        st.session_state.message = (
            "문은 굳게 잠겨 있다.\n"
            "옆에 숫자를 입력하는 장치가 붙어 있다."
        )

    else:

        st.session_state.message = (
            "문 옆의 비밀번호 입력 장치를 발견했다.\n"
            "금고에서 얻은 단서를 사용해야 할 것 같다."
        )

    st.rerun()


# ============================================================
# 힌트
# ============================================================

st.divider()

with st.expander("💡 힌트"):

    if not st.session_state.key_found:

        st.write(
            "힌트 1: 교실 안의 가구를 자세히 조사해보자."
        )

    elif not st.session_state.clue_found:

        st.write(
            "힌트 2: 칠판에 무언가 적혀 있다."
        )

    elif not st.session_state.safe_open:

        st.write(
            "힌트 3: 낡은 열쇠는 금고에 사용할 수 있다."
        )

    else:

        st.write(
            "힌트 4: 칠판에는 '답은 거꾸로 보아라'라고 적혀 있다."
        )

    st.write(
        "최종적으로 입력해야 하는 숫자는 "
        "**4862**이다."
    )


# ============================================================
# 게임 설명
# ============================================================

with st.expander("📖 게임 정보"):

    st.write("""
    **게임 목표**

    3분 안에 폐교의 교실에서 탈출하세요.

    **공략 순서**

    1. 교탁 서랍 조사
    2. 낡은 열쇠 획득
    3. 금고 조사
    4. 금고에서 숫자 2684 확인
    5. 칠판의 "거꾸로 보아라"라는 힌트 확인
    6. 문 비밀번호에 4862 입력
    7. 탈출 성공

    **제작 방식**

    이 게임은 Streamlit의 `session_state`를 이용하여
    아이템, 퍼즐, 진행 상황을 관리합니다.
    """)


# ============================================================
# 시간 갱신
# ============================================================

time.sleep(1)
st.rerun()
