import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    return pd.read_csv('cars.csv')

# Main function to run the Streamlit app
def main():
    st.title('Car Details Based on Budget')
    
    # Load data
    df = load_data()

    # Input for budget
    budget = st.slider('Select your budget', min_value=1000, max_value=100000, step=1000)

    # Filter cars based on budget
    filtered_cars = df[df['Price'] <= budget]

    if not filtered_cars.empty:
        st.write(f'Cars available within your budget (${budget}):')
        st.dataframe(filtered_cars)
    else:
        st.write(f'No cars available within your budget (${budget}).')

if __name__ == '__main__':
    main()
