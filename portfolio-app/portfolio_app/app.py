import streamlit as st
from streamlit_option_menu import option_menu
from about_me import about_me
from experience import experience

### Set layout page to wide
st.set_page_config(layout='wide')


def menu():
    with st.sidebar:
        selected = option_menu(
            menu_title='Flavia Ferreira',
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
    

if __name__ == "__main__":
    selected = menu()
    if selected == "About Me":
        about_me()
    elif selected == "Experience":
        experience()
        
