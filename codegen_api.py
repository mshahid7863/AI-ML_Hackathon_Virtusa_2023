import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/generate-code', methods=['POST'])
def generate_code():
    data = request.json
    tool = data['tool']
    language = data['language']
    prompt = data['prompt']

    # Create the prompt template
    full_prompt = f"Generate a test automation script using {language} programming language with {tool} for the " \
                  f"following scenario: {prompt}"

    # Call OpenAI API
    openai_response = call_openai_api(full_prompt)

    return openai_response


def call_openai_api(prompt):
    openai_api_key = os.getenv('API_KEY')  # Enter the API Key
    openai_api_url = os.getenv('API_URL')  # Enter the API URL
    headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'messages': [{'role': 'system',
                      'content': 'Act as a Test Automation Architect expert in various Test Automation Frameworks. '
                                 'The user will be providing inputs like tool, programming language and the steps '
                                 'needed for the script to cover and you have to provide clear and executable test '
                                 'script. Use id and xpath as the preferred element locator methods for browser '
                                 'automation. Use BDD model script for Rest Assured tool. '
                                 'In case of SQL, write detailed query with the best join and aggregate functions possible.'
                                 'Use appropriate design pattern wherever possible'},
                     {'role': 'user', 'content': prompt}],
        # 'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 500,
        'model': 'gpt-3.5-turbo'
    }
    print(data)
    response = requests.post(openai_api_url, headers=headers, json=data)
    print(response.json())
    return response.json()['choices'][0]['message']['content']


if __name__ == '__main__':
    app.run(debug=True)
