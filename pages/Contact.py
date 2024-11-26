import streamlit as st 
from send_email import send_email
st.header('Contact Me')

with st.form(key="form"):
    user_email = st.text_input("Your Email Address: ")
    msg_text = st.text_area("Your Message: ")
    msg_text = f"""\
        
        Subject: {user_email}
        
        {msg_text}
    """
    
    button = st.form_submit_button("Submit")
    
    if button:
        send_email(msg_text)
        st.info("Your email is send successfully")