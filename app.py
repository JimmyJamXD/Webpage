import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#User Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")

#Load Assets
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_shoe = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_projects = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_hrkmmhjf.json")


#Header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Hi I am Jimmy :wave:")
        st.header("A little about me")
        st.write("Aspiring Computer Engineer, learning and coding when I have the time")
        st.write("Languages I know: C++, C#, Python, HTML, CSS, and Javascript")
        st.write("""Graduate from California State Polytechnic University with a bachelor
        degree in Computer Engineering""")

    with right_column:
        st_lottie(lottie_shoe, height=300, key="coding")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2, gap="small")
    with left_column:
        st.title("Job Experiences")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("1st Job")
        st.write("Worked at D2Moto")
        st.write("Job title: Packager")
        st.text("""Description: Packaging and shipping orders 
             for customer and perform a quality 
             check before shipping. """)
    with col2:
        st.header("2nd Job")
        st.write("Premio Inc")
        st.write("Job title: Field Application Engineer")
        st.text("""Description: Troubleshooting and resolving technical
             problem for company's product and
             customer's product. """)
        
    with col3:
        #    st.markdown('Streamlit is **_really_ cool**.')
        st_lottie(lottie_coding, height=300, key="noncode") 

with st.container():
    st.write("---")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.title("My Profile") 
    
    column1, column2, column3 = st.columns(3)
    with column1:
        st.header("Website Links")
        st.write("Linkedin: (https://www.linkedin.com/in/jimmy-ngo-23b2031a1/)")
        st.write("Github: (https://github.com/JimmyJamXD)")
        
    with column3:
        st_lottie(lottie_projects, height=250, key="noncoding")
        

with st.container():
    st.write("---")
    st.header("Contact Me")
        
    contact_form = """ 
        <form action="https://formsubmit.co/jimmyngo12@email.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder= "Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
            st.empty()
