import csv
import openai

# Setup OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# 1. Read the CSV file
csv_file = '01-2023-3-15-2023 result.csv'
text_column_name = 'text'

with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Loop through each row in the CSV
    for row in reader:
        text = row[text_column_name]

        # Set up a conversation with GPT-3.5-turbo
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"The following text is a comment about the Energiepauschale. What are the general feelings of the people who commented? \"{text}\""}
        ]

        # 2. Interact with ChatGPT via OpenAI Python module
        try:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=messages
            )

            emotion = response.choices[0].message['content'].strip()
            print(f"Text: {text}\nEmotion: {emotion}\n")

        except openai.error.OpenAIError as err:
            print(f"API request failed for text: \"{text}\"")
            print(f"Error message: {err}")
            print("-" * 50)
