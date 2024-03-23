import json
import requests
import streamlit as st
<<<<<<< HEAD
from streamlit_lottie import st_lottie 
  
  
url = requests.get( 
    "https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json") 
url_json = dict() 
if url.status_code == 200: 
    url_json = url.json() 
else: 
    print("Error in URL") 
=======
from streamlitlottie import st_lottie
st.set_page_config(page_title = "My page",page_icon =":tada:",layout = "wide")
def load_lottieurl(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
>>>>>>> 2581bb0ac0915c86fbae1cd83a89838089b71dce
#---- LOAD ASSERTS-----
lot_code = load_lottieurl("animations/aaa1.json")

#------Header-------
with st.container():
    st.subheader("Hi i am sanket :wave:")
    st.title("A noraml human")
    st.write("I am a simple who want to test thid python libaray")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Whta I do")
        st.write("##")
        st.write("""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).""")
        st.write("[see more](https://github.com/Sanket794/streamlitrepo/blob/main/app.py)")
    with right_column:
<<<<<<< HEAD
        st_lottie(url_json, 
          # change the direction of our animation 
          reverse=True, 
          # height and width of animation 
          height=400,   
          width=400, 
          # speed of animation 
          speed=1,   
          # means the animation will run forever like a gif, and not as a still image 
          loop=True,   
          # quality of elements used in the animation, other values are "low" and "medium" 
          quality='high', 
           # THis is just to uniquely identify the animation 
          key='Car' 
          ) 
=======
        st_lottie(lot_code,height = 300, key = "coding")
>>>>>>> 2581bb0ac0915c86fbae1cd83a89838089b71dce
    

