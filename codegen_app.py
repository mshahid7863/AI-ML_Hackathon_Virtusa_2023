import streamlit as st
import requests


# Custom CSS to inject into the Streamlit app
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Use the local_css function to load the CSS file
local_css('style.css')

# Set up the title and user prompt input
st.markdown("<h1 style='text-align: center; color: black;'>Test Automation CodeGen App</h1>", unsafe_allow_html=True)

# Define the Streamlit UI layout
# st.title('Please enter the following and Click Generate')
st.subheader('Please enter the following and click :blue[Generate] :sunglasses:')

# Dropdown for selecting the tool
tool = st.selectbox('Tool', ['Selenium', 'Playwright', 'Cypress', 'Robot', 'Rest Assured', 'SQL'])

# Dropdown for selecting the language
language = st.selectbox('Language', ['java', 'python', 'javascript', 'sql'])

# Input textbox for the user's prompt
user_prompt = st.text_area('Please enter the steps', height=50)

# Output textbox for displaying generated code
output = st.empty()  # placeholder for the output


# Function to send data to Flask API and get the generated code
def generate_code(tool, language, prompt):
    # Assuming the Flask API is running on localhost and listening on port 5000
    api_url = "http://localhost:5000/generate-code"
    data = {'tool': tool, 'language': language, 'prompt': prompt}

    response = requests.post(api_url, json=data)
    return response.text


# Button to generate code
if st.button('Generate'):
    generated_code = generate_code(tool, language, user_prompt)
    output.text_area('Output', value=generated_code, height=300)
