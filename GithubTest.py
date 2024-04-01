import streamlit as st
st.write('Welcome to UNCC')
money = ['yes', 'no']
unccmoney = st.text_input('Will classes will be cheap?')
if st.button('Press to make money disappear'):
    tuition = unccmoney.lower() in money
    'Tutition went up again' if tuition else 'This was a yes or no question. How did you get here?'
st.image('norm.jpg')
st.audio('fight_song.mp3')
st.radio('Are you going to class?',['Sit in traffic for an hour', 'Stay home and regret it'])
st.color_picker('Choose green or you will be THROWN OUT')