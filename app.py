import streamlit as st
import random
from PIL import Image

def guess_number():
    st.write("# Guess the number and get a birthday surprise!")
    st.write("Choose a number between 1 and 10:")
    number = st.number_input("", min_value=1, max_value=10, step=1, key="number_input")
    if st.button("Guess"):
        if random.randint(1, 3) == number:
            st.write("## 🎉 Congratulations! You guessed the correct number. 🎉")
            st.write("Happy Birthday! 🎂🎈 May all your dreams come true and may this year bring you lots of joy, happiness and success. Enjoy your special day! 🎁🥳")
            banner_img = Image.open("banner.jpg")
            st.image(banner_img, use_column_width=True)
            cake_img = Image.open("cake.jpg")
            st.image(cake_img, use_column_width=True)
        else:
            st.write("Sorry, that's not the correct number. Try again!")
            
    st.write("Click the button below to claim your gift!")
    if st.button("Get Your Gift"):
            st.write("Redirecting to gift page...")
            # Replace the URL below with the actual URL of the gift page
            st.redirect("https://www.example.com/birthday-gift")
            
if __name__ == "__main__":
    guess_number()
