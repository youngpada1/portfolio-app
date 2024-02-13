#!/usr/local/bin/python

import streamlit as st
from streamlit import runtime
from streamlit.web import cli
from streamlit_option_menu import option_menu

from portfolio_app import about_me, experience

### Set layout page to wide
st.set_page_config(layout='wide')


def menu():
    with st.sidebar:
        selected = option_menu(
            menu_title='Your Name',
            menu_icon='pages', default_index=0,
            options=['About Me', 'Experience'],
            #orientation='horizontal',
            styles={
        'container': {'padding': '5!important', 'background-color': '#000000'},
        'icon': {'color': 'orange', 'font-size': '10px'}, 
        'nav-link': {'font-size': '12px', 'text-align': 'left', 'margin':'0px', '--hover-color': '#eee'},
        'nav-link-selected': {'background-color': '#000000'},
            })
        return selected

def app():
    selected = menu()
    if selected == "About Me":
        about_me()
    elif selected == "Experience":
        experience()


def main():
    """Execute with streamlit"""
    if runtime.exists():
        app()
    else:
        import sys

        sys.argv = [
            "streamlit",
            "run",
            __file__,
            "--server.headless=true",
            "--server.enableXsrfProtection=false",
            "--server.enableCORS=false",
        ]
        st.write("Relaunching...")
        sys.exit(cli.main())

if __name__ == "__main__":
    main()        
