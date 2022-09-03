import os
import yaml
import init_streamlit
import streamlit as st
import libs.streamlit_authenticator as stauth

st.set_page_config(page_title='懒编程',
                   page_icon='logo.jpg')

st.title('hello world')


def init_authenticator():
    filepath = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(filepath, 'auth.yaml')) as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
    )
    return authenticator


def register_user(authenticator):
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)


def my_logics():
    st.markdown('login success')


def start_web():
    authenticator = init_authenticator()
    # check cookie not login again
    authenticator._check_cookie()
    if st.session_state["authentication_status"]:
        authenticator.logout('Logout', 'sidebar')
        my_logics()
    else:

        tab1, tab2 = st.tabs(["Login", "Register"])
        with tab1:
            name, authentication_status, username = authenticator.login(
                'Login', 'main')
            if st.session_state["authentication_status"] == False:
                st.error('Username/password is incorrect')
            elif st.session_state["authentication_status"] == None:
                st.warning('Please enter your username and password')
        with tab2:
            register_user(authenticator)

start_web()