import streamlit as st
import os, base64
import pandas as pd
from pathlib import Path
from PIL import Image

# st.set_page_config(layout='wide')

def about_me():
# Set layout page to wide
        

        # Adding introductory message
        st.title('Your Name')
        st.markdown('''Introduction Text''')
        st.write('''___''')

        # Adding columns
        col1, col2, col3, col4 = st.columns(4)
        # Profile photo section
        with col1: 
            profile_pic = "https://raw.githubusercontent.com/youngpada1/portfolio-app/9fcb7438c028c7517786155b5be9cd1fc517447e/portfolio-app/portfolio_app/images/menu/profile%20icon.png"
            st.image(profile_pic, width=100)

        # Download resume
        with col2:
            resume = Path(__file__).parent / Path('images/menu/resume-template.pdf') #Resume
            #loading resume in PDF Formatß
            with open(resume, 'rb') as f:
                bytes_data = f.read()
        # Adding download button
            st.download_button( 
            label='Download Resume',
            data=bytes_data,
            file_name='Your Name | Resume',
            mime='application/pdf',
            key='download'
        )
        # Link to Github

        with col3:
            github = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/github.png'
            st.markdown(f'''
            <a href='https://github.com'>
                <img src='{github}' width='25px'/>
            </a>''',
            unsafe_allow_html=True
        )

        # Link to LinkedIn
        with col4:
            linkedin = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/linkedin.png' #LinkedIn profile
            st.markdown(f'''
            <a href='https://www.linkedin.com/'>
                <img src='{linkedin}' width='20px'/>
            </a>''',
            unsafe_allow_html=True
        )

        # Page Intro    
        st.write('Add brief description of your who you are and your career experiences')
        st.write(''' ''')

        # Adding link (Photos and Hyperlinks)
        st.subheader('Other Links')


        # Organizing links per column
        col1, col2, col3= st.columns(3)

        # Streamlit Link 1
        with col1:
            streamlit_link1 = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/streamlit.png'
            col1.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.attackmagazine.com/features/interview/5-women-in-the-synthesizer-industry-flavia-ferreira-focusrite/'>
                        <img src='{streamlit_link1}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        # Streamlit Link 2
        with col2:
            streamlit_link2 = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/streamlit.png'
            col2.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.elektormagazine.com/articles/women-in-tech'>
                        <img src='{streamlit_link2}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        # Streamlit Link 3
        with col3:
            streamlit_link3 = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/streamlit.png'
            col3.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.instagram.com/reel/Ct1yGcQoE91/'>
                        <img src='{streamlit_link3}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        st.write('''''') #Space between mag links & Youtube Videos

        # Adding Youtube Videos
        col1, col2, col3 = st.columns(3)
        # Video 1 
        with col1:
            col1.markdown('Video Title')
            streamlit_video = st.video('https://youtu.be/JSeQSnGovSE?feature=shared')
        # Video 2 
        with col2:
            col2.markdown('Video Title')
            streamlit_video1 = st.video('https://youtu.be/YaFvCwjk-_A?feature=shared')
        # Video 3 
        with col3:
            col3.markdown('Video Title')
            streamlit_video3 = st.video('https://youtu.be/vzlQkAzWCeI?feature=shared')
    

    


            