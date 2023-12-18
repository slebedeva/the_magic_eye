import streamlit as st
import random

st.set_page_config(page_title="The Magic Eye"
                   , page_icon="👀"
                   , layout="centered"
                   #, initial_sidebar_state="auto"
                   , menu_items={
        'Get Help': 'https://github.com/slebedeva/the_magic_eye',
        'Report a bug': "https://github.com/slebedeva/the_magic_eye/issues",
        'About': "This is a digital copy of a physical all seeing Eye. All rights reserved for the original designer. No liability for consequence of predictions."
    })

@st.cache(ttl=3600) # the Eye will remember its answer for 1 hour
def answer(question):
    """
    Pick a random answer among 16.
    """

    possible_answers=[
    "absolutely"
    ,"answer unclear ask later"
    ,"cannot foretell now"
    ,"can't say now"
    ,"chances aren't good"
    ,"consult me later"
    ,"don't bet on it"
    ,"focus and ask again"
    ,"indications say yes"
    ,"looks like yes"
    ,"no"
    ,"no doubt about it"
    ,"positively"
    ,"prospect good"
    ,"so it shall be"
    ,"the stars say no"
    ,"unlikely"
    ,"very likely"
    ,"yes"
    ,"you can count on it"
    ]

    idx = random.randint(0, len(possible_answers))
    return possible_answers[idx].upper()

st.header('The Magic Eye')

col1, col2 =  st.columns(2)

with col1:
    st.image('eye.png')

with col2:
    st.markdown('The all-seeing Eye will tell you about your future.')

    question = st.text_input("Shake the Eye and ask a Yes/No question:")

    if st.button('Answer'):

        st.write(answer(question))
