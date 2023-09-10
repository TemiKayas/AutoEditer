import openai
import json
import re

API_KEY=open("API_KEYS.env", "r")
openai.api_key = API_KEY.read()

# Key points method
def extract_key_points(json_filename, api_key):
    # Load the JSON data
    #Tryed changing the file name from json_file name to current. If pathing isnt correct just reset it
    with open("./output/transcript.json", 'r') as file:
        transcription_entries = json.load(file)

    # Concatenate the text from the transcription entries
    transcript_text = ' '.join([entry['text'] for entry in transcription_entries])

    # Set the OpenAI API key
    openai.api_key = api_key

    # Generate key points using the OpenAI API
    try:
        key_points_response = openai.Completion.create(
            engine="davinci",
            prompt=f"Extract key points from the following text: {transcript_text}",
            max_tokens=150,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"],
            n=1,
        )
        key_points = key_points_response.choices[0].text.strip().split('\n')
        
        # Extract direct quotes associated with the key points
        key_point_quotes = {}
        for key_point in key_points:
            key_point_quote = ""
            words = key_point.split()
            for word in words:
                for entry in transcription_entries:
                    if word in entry['text']:
                        key_point_quote += f"{word} "
                        break
            key_point_quotes[key_point] = key_point_quote.strip()
        
        return key_point_quotes
    except Exception as e:
        print(f"Error extracting key points: {e}")
        return None

# Use the method to extract key points and their associated direct quotes
json_filename = "./output/transcript.json"
api_key = openai.api_key
key_point_quotes = extract_key_points(json_filename, api_key)
print(key_point_quotes)

