import streamlit as st 
import pandas

st.set_page_config(layout="wide")

cols1,space,cols2 = st.columns([3,1,3])

with cols1:
    st.image("./Images/p.jpg", width=300)
    
with cols2:
    st.title("PRASHANT ADHIKARI(CODY)")
    content = """
    Hi,I am a passionate BCA student and lifelong learner, driven by curiosity and a love for problem-solving. I actively explore programming languages, embrace challenges, and enjoy creating innovative software solutions. With a collaborative mindset, I seek opportunities to contribute to impactful projects and grow in the dynamic field of computer science.
    """
    st.info(content)
    
content2 = """
Below you can find some of my project built in different programming language.
"""
st.info(content2)

# create column and add space between the cell
cols3,space,cols4 = st.columns([3,1,3])

df = pandas.read_csv("dataset.csv", sep=";")

with cols3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"], width=200)
        st.write(f"[Souce Code]({row['url']})")

with cols4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"], width=200)
        st.write(f"[Souce Code]({row['url']})")
        
content3 = """
Follow Me On:
"""
st.info(content3)
st.write("[GitHub](https://github.com/iamcody-git)")  
st.write("[LinkedIn](https://www.linkedin.com/in/prashant-adhikari009/)")