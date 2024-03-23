import streamlit as st

st.set_page_config(page_title = "My page",page_icon =":tada:",layout = "wide")

#------Header-------
with st.container():
    st.subheader("Hi i am sanket :wave:")
    st.title("A noraml human")
    st.write("I am a simple who want to test thid python libaray")
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    for i in range(0,3):
        with left_column():
            st.header("Whta I do")
            st.write("##")
            st.write("""It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).""")
            st.write("[see more](https://github.com/Sanket794/streamlitrepo/blob/main/app.py)")

