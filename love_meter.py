import streamlit as st
import random

# Function to generate a love score and message
def generate_love_score(name1, name2):
    # Simple random number generator to simulate a love score
    random.seed(name1 + name2)  # Seed random number generator for reproducibility
    score = random.randint(50, 100)  # Generate a score between 50 and 100

    # Generate a fun message based on the score
    if score >= 90:
        message = "You're a match made in heaven! 💕"
    elif score >= 70:
        message = "Great match! You two are quite compatible. 😍"
    elif score >= 50:
        message = "There's potential here! Keep working on it. 😊"
    else:
        message = "It's a work in progress. Keep the love alive! ❤️"

    return score, message

# Main function to run the Streamlit app
def main():
    st.title('Love Meter')

    # Input fields for names
    name1 = st.text_input('Enter your name')
    name2 = st.text_input('Enter your spouse\'s name')

    # Generate love score and message if both names are provided
    if name1 and name2:
        score, message = generate_love_score(name1, name2)
        st.write(f"**Love Score between {name1} and {name2}:**")
        st.write(f"{score}%")
        st.write(message)
    else:
        st.write("Please enter both your name and your spouse's name.")

if __name__ == '__main__':
    main()
