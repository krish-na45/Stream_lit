import streamlit as st

# Function to generate potential child names
def generate_child_name(parent1, parent2):
    # Simple logic to combine parts of the parents' names
    if parent1 and parent2:
        part1 = parent1[:len(parent1)//2]
        part2 = parent2[len(parent2)//2:]
        name1 = part1 + part2
        name2 = part2 + part1
        return [name1.capitalize(), name2.capitalize()]
    return []

# Main function to run the Streamlit app
def main():
    st.title('Child Name Generator')

    # Input fields for parents' names
    parent1 = st.text_input('Enter your name')
    parent2 = st.text_input('Enter your spouse\'s name')

    # Generate child names if both parents' names are provided
    if parent1 and parent2:
        child_names = generate_child_name(parent1, parent2)
        if child_names:
            st.write(f"**Potential child names based on {parent1} and {parent2}:**")
            for name in child_names:
                st.write(name)
        else:
            st.write("Please enter both names.")
    else:
        st.write("Please enter both your name and your spouse's name.")

if __name__ == '__main__':
    main()
