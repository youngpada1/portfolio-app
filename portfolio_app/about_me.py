import streamlit as st
from pathlib import Path

def about_me(about_me_data, source_path):
# Set layout page to wide
        
        name = about_me_data.get('name', 'Your Name')
        # Adding introductory message
        st.title(name)
        if "intro" in about_me_data:
            st.markdown(about_me_data["intro"])
        st.write('''___''')

        # Adding columns
        col1, col2, col3, col4 = st.columns(4)
        # Profile photo section
        with col1: 
            if "profile_pic" in about_me_data:
                st.image(about_me_data["profile_pic"], width=100)

        # Download resume
        with col2:
            if "resume" in about_me_data:
                resume = source_path / Path(about_me_data["resume"])
                #loading resume in PDF Formatß
                with open(resume, 'rb') as f:
                    bytes_data = f.read()
            # Adding download button
                st.download_button( 
                    label='Download Resume',
                    data=bytes_data,
                    file_name=f'{name} | Resume',
                    mime='application/pdf',
                    key='download'
                )
        # Link to Github

        with col3:
            if "github" in about_me_data:
                github_logo = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/github.png'
                st.markdown(f'''
                    <a href='{ about_me_data["github"]}' target='_blank'>
                        <img src='{github_logo}' width='25px'/>
                    </a>''',
                    unsafe_allow_html=True
                )

        # Link to LinkedIn
        with col4:
            if "linkedin" in about_me_data:
                linkedin_logo = 'https://raw.githubusercontent.com/youngpada1/portfolio-app/efa44604e838ff5218db9a9229b8fff256df5ae6/portfolio-app/portfolio_app/images/menu/linkedin.png' #LinkedIn profile
                st.markdown(f'''
                    <a href='{ about_me_data["linkedin"]}' target='_blank'>
                        <img src='{linkedin_logo}' width='20px'/>
                    </a>''',
                    unsafe_allow_html=True
                )

        # Page Intro
        if "Intro" in about_me_data:
            st.write(about_me_data["intro"])
    
        st.write(''' ''')

        # Adding link (Photos and Hyperlinks)
        if "links" in about_me_data:
            links = about_me_data["links"]
            st.subheader('Other Links')

            # Organizing links per column
            cols = st.columns(len(links))

            for i, col in enumerate(cols):

                with col:
                    try:
                        title = links[i]["title"]
                        url = links[i]["url"]
                        image = links[i]["image"]
                    except KeyError as exc:
                        st.error(f"'{exc}' property missing for link #{i}")
                        continue

                    col.markdown(f'''
                                { title }
                                <a href='{url}'>
                                <img src='{image}' width=100%/>
                                </a>''',
                                unsafe_allow_html=True
                                )
            st.write('''''') #Space between links & Youtube Videos

        if "youtube" in about_me_data:
            # Adding Youtube Videos
            youtube = about_me_data["youtube"]
            cols = st.columns(len(youtube))
            
            for i, col in enumerate(cols):
                with col:
                    try:
                        st.markdown(youtube[i]["title"])
                        st.video(youtube[i]["url"])
                    except KeyError as exc:
                        st.error(f"'{exc}' property missing for youtube video #{i}")
                        continue
