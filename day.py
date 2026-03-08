import streamlit as st

st.set_page_config(page_title="Поздравительная игра")

st.title("Добро пожаловать в игру 🎈")

passwords = [
    "первый",
    "пароль",
    "всегда",
    "нужен",
    "только",
    "для",
    "теста"
]

if "step" not in st.session_state:
    st.session_state.step = 1


for i in range(1,8):

    if st.session_state.step >= i:

        st.write("Это твой вопрос и ты должна на него ответить")

        answer = st.text_input(
            "Введите пароль",
            key=f"input{i}",
            type="password"
        )

        if st.button("Вперед", key=f"btn{i}"):

            # проверка без учета регистра
            if answer.lower() == passwords[i-1]:

                st.success("Правильно! 🎉")

                if st.session_state.step == i:
                    st.session_state.step += 1

            else:
                st.error("Неверный пароль")


if st.session_state.step == 8:
    st.balloons()
    st.success("🎉 Поздравляю! Ты прошла весь квест! 🎉")
