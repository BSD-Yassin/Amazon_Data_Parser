import streamlit

header = st.beta.container()
dataset = st.beta.container()

with header:
    st.title('Welcome to my science project')
    st.text('In this project I will learn about streamlit')

with dataset:
    st.header('Dataset')

with features:
    st.header('The features I created')

with model_training:
    st.header('Dataset')