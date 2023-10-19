import openai
import json

api_key=open("API_KEYS.env", "r")
openai.api_key = api_key.read()  

def call_chatgpt_v4(api_key, user_message, transcript_chunk):
    
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Rate the relevance of the chunk to the query between 0 (not relevant) and 1 (highly relevant)."},
            {"role": "user", "content": f"Query: {user_message}\nChunk: {transcript_chunk}"}
        ]
    )
    
    response = completion.choices[0].message['content']
    try:
        relevance_score = float(response)
    except ValueError:
        relevance_score = 0  # Higher the relevance score the more words must match

    return relevance_score

def search_transcript_for_quote(api_key, query, keyword):
    with open("./output/transcript.json", "r") as file:
        transcripts = json.load(file)

    # Filter transcripts based on the keyword
    potential_matches = [entry for entry in transcripts if keyword.lower() in entry["text"].lower()]

    if not potential_matches:
        return None

    highest_relevance_score = 0
    most_relevant_entry = None

    # Use ChatGPT to evaluate relevance for each potential match
    for entry in potential_matches:
        relevance_score = call_chatgpt_v4(api_key, query, entry["text"])

        if relevance_score > highest_relevance_score:
            highest_relevance_score = relevance_score
            most_relevant_entry = entry

    return most_relevant_entry["id"]


quote_id = search_transcript_for_quote(api_key, "The text discusses the idea of developing a software that can automatically edit videos by condensing them and summarizing key points", "edit")
if quote_id:
    print(f"Relevant quote found with ID: {quote_id}")
else:
    print("No relevant quote found in the transcript.")
