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
            github = 'https://raw.githubusercontent.com/youngpada1/padawanapp/a98515a589676598e3ff4fa18a3c24d6f23971b8/padawapp/images/github.png'
            st.markdown(f'''
            <a href='https://github.com'>
                <img src='{github}' width='20px'/>
            </a>''',
            unsafe_allow_html=True
        )

        # Link to LinkedIn
        with col4:
            linkedin = 'https://raw.githubusercontent.com/youngpada1/padawanapp/a98515a589676598e3ff4fa18a3c24d6f23971b8/padawapp/images/linkedin.png' #LinkedIn profile
            st.markdown(f'''
            <a href='https://www.linkedin.com/'>
                <img src='{linkedin}' width='20px'/>
            </a>''',
            unsafe_allow_html=True
        )

        # Page Intro    
        st.write('Add brief description of your who you are and your career experiences')
        st.write(''' ''')

        # Adding link to interviews (Media)
        st.subheader('Other Links')


        # Organizing links per column
        col1, col2, col3= st.columns(3)

        # Attack Mag
        with col1:
            streamlit_link1 = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Attack%20Mag.png'
            col1.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.attackmagazine.com/features/interview/5-women-in-the-synthesizer-industry-flavia-ferreira-focusrite/'>
                        <img src='{streamlit_link1}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        # Elektor Mag
        with col2:
            elektor = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Elektor%20Mag.png'
            col2.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.elektormagazine.com/articles/women-in-tech'>
                        <img src='{elektor}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        # Instagram
        with col3:
            instagram = 'https://raw.githubusercontent.com/youngpada1/padawanapp/c1fbfe2975240555c9dd6968ae8ada7962da0551/padawapp/images/Focusrite.jpeg'
            col3.markdown('Link Title')
            st.markdown(f'''
                        <a href='https://www.instagram.com/reel/Ct1yGcQoE91/'>
                        <img src='{instagram}' width=100%/>
                        </a>''',
                        unsafe_allow_html=True
                        )

        st.write('''''') #Space between mag links & Youtube Videos

        # Adding Youtube Videos
        col1, col2, col3 = st.columns(3)
        # Video 1 - Octatrack
        with col1:
            col1.markdown('Video Title')
            octa_video = st.video('https://youtu.be/i4GFGXrruok')
        # Video 2 - Atari
        with col2:
            col2.markdown('Video Title')
            atari_video = st.video('https://www.youtube.com/watch?v=glaTan_GPs0')
        # Video 3 - Octatrack
        with col3:
            col3.markdown('Video Title')
            eurorack_video = st.video('https://www.youtube.com/watch?v=l1DEk35WWA8')
    

    


            