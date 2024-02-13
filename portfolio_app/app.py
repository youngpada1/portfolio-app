#!/usr/local/bin/python

import argparse
import pathlib
import yaml
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

def app(source):
    portfolio = yaml.load(source.open(), Loader=yaml.BaseLoader)
    selected = menu()
    if selected == "About Me":
        about_me(portfolio.get("about_me"), source_path=source.parent)
    elif selected == "Experience":
        experience(portfolio.get("experience"))


def main():
    
    parser = argparse.ArgumentParser(
                    prog='Portfolio App',
                    description='Serve your portfolio as a streamlit',
                    epilog='Brought to you by youngpada1')

    parser.add_argument('portfolio', type=pathlib.Path, help="Path to the YAML portfolio file")
    args = parser.parse_args()

    if runtime.exists():
        app(args.portfolio)
    else:
        import sys

        sys.argv = [
            "streamlit",
            "run",
            __file__,
            "--server.headless=true",
            "--server.enableXsrfProtection=false",
            "--server.enableCORS=false",
            str(args.portfolio),
        ]
        st.write("Relaunching...")
        sys.exit(cli.main())

if __name__ == "__main__":
    main()        
