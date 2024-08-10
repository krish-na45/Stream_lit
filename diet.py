import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

# Function to determine weight status and provide diet plan
def get_weight_status_and_diet_plan(bmi):
    if bmi < 18.5:
        status = "Underweight"
        diet_plan = "Focus on calorie-dense foods. Include healthy fats and proteins in your diet. Consider consulting a nutritionist for a personalized plan."
    elif 18.5 <= bmi < 24.9:
        status = "Normal"
        diet_plan = "Maintain a balanced diet with a mix of carbohydrates, proteins, and fats. Regular exercise is recommended for overall health."
    else:
        status = "Overweight"
        diet_plan = "Consider a diet plan with reduced calorie intake. Focus on lean proteins, vegetables, and whole grains. Regular exercise is also recommended. Consult a nutritionist for a personalized plan."
    return status, diet_plan

# Main function to run the Streamlit app
def main():
    st.title('BMI and Diet Plan Calculator')

    # Input fields
    name = st.text_input('Name')
    height = st.number_input('Height (in cm)', min_value=0.0, format="%.1f")
    weight = st.number_input('Weight (in kg)', min_value=0.0, format="%.1f")
    age = st.number_input('Age', min_value=0, format="%d")

    # Ensure height and weight are provided
    if height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        status, diet_plan = get_weight_status_and_diet_plan(bmi)

        st.write(f'**Name**: {name}')
        st.write(f'**Height**: {height} cm')
        st.write(f'**Weight**: {weight} kg')
        st.write(f'**Age**: {age} years')
        st.write(f'**BMI**: {bmi:.1f}')
        st.write(f'**Weight Status**: {status}')
        st.write('**Diet Plan**:')
        st.write(diet_plan)
    else:
        st.write("Please enter both height and weight.")

if __name__ == '__main__':
    main()
