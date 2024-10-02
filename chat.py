import os #for api key
from groq import Groq
import streamlit as st

st.title("Enter the food item to give the recipe of:")

food=st.text_input("")
if st.button("Search"):
    client = Groq(
        api_key="",
        #API KEY GOES IN THERE
    )
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role":"system",
                "content":"you give step by step bullent points . If the item is not food, tell it is not a food item"
            },
            {
                "role": "user",
                "content": "Make a step by step recipe to make a "+food+"\n"
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )
    final=""
    for chunk in completion:
        final+=(chunk.choices[0].delta.content or "")

    st.write(final)
else:
    st.write("Waiting for input...")