import streamlit as st

st.set_page_config(page_title="Поздравительный квест")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
    background: linear-gradient(135deg,#ffd1dc,#d1ffd6,#d1e0ff);
}

h1, h2, h3 {
    color:#cd7f32;
    text-align:center;
}

div.stTextInput > div > div > input {
    border:1px solid green;
}

.block{
    background:white;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
}

.final{
    background:white;
    padding:40px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    box-shadow:0 0 20px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

st.title("Добро пожаловать в игру 🎈")

questions = [
("Это твой вопрос и ты должна на него ответить","первый"),
("Кто едет","пароль"),
("Где рыба","всегда"),
("Как прыгать","нужен"),
("Когда быть","только"),
("Куда лететь","для"),
("За кем бежать","теста")
]

if "step" not in st.session_state:
    st.session_state.step = 0


for i,(q,answer) in enumerate(questions):

    if st.session_state.step >= i:

        st.markdown('<div class="block">', unsafe_allow_html=True)

        st.subheader(f"{i+1}. {q}")

        user = st.text_input(
            "Введите пароль",
            key=f"input{i}"
        )

        if st.button("Вперед", key=f"btn{i}"):

            if user.lower() == answer:

                st.success("Правильно!")

                if st.session_state.step == i:
                    st.session_state.step += 1
                    st.rerun()

            else:
                st.error("Неверный пароль")

        st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.step == 7:

    st.markdown("""
    <div class="final">
    🎉 Поздравляю! Ты прошла квест! <br><br>
    Твой подарок — Шкаф 🎁
    </div>
    """, unsafe_allow_html=True)
