import json
import openai

def search_transcript_with_gpt(query, json_filename):
    """
    Use ChatGPT to search for a specific query in the transcript and return the IDs of relevant quotes.
    
    Args:
    - query (str): The user's search query.
    - json_filename (str): The name of the JSON file containing the transcript.
    
    Returns:
    - list: A list of IDs corresponding to the relevant quotes as determined by ChatGPT.
    """

    matching_ids = []

    # Load the JSON data
    #Changed json_filename to path for transcript.json
    with open("./output/transcript.json", 'r') as file:
        transcript_entries = json.load(file)

    # Initialize OpenAI API
    API_KEY=open("API_KEYS.env", "r")
    openai.api_key = API_KEY.read()  # Replace with your API key


    #Try sending entire transcript and having it search through the entire transcript
    #Cut start and end time stamps from the transcript before sending it
    for entry in transcript_entries:
        prompt = f"Given the query '{query}', is the following quote relevant? \"{entry['text']}\""
        ##Use Davinci instead of GPT 4
        response = openai.Completion.create(
            model="gpt-4",  # This might change depending on available models in the future
            prompt=prompt,
            max_tokens=50  # Limiting the response length for brevity
        )
        
        if "yes" in response.choices[0].text.lower():
            matching_ids.append(entry['id'])

    return matching_ids

# Test the method
json_filename = "transcription.json"
query = input("Please enter your search query: ")
matching_ids = search_transcript_with_gpt(query, json_filename)

if matching_ids:
    print(f"Found relevant quotes with the following IDs: {matching_ids}")
else:
    print("No relevant matches found.")
