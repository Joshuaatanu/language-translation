import streamlit as st


def translate_sentence(sentence, translation_dict):
    translated_sentence = translation_dict.get(sentence)
    return translated_sentence


# load translation dictionary
translation_dict = {
    "hello": "Jambo",
    "how are you": "habari gani?",
    "you look good": "Unapendeza"
}
# streamit UI
st.title("english to Swahili translator")

input_text = st.text_input("Enter your english:")
if input_text:
    translated_text = translate_sentence(input_text, translation_dict)
    st.write("Swahili translation:", translated_text)
