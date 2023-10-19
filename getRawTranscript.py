import json

def extract_text_from_transcript_file(filename):
    with open(filename, 'r') as file:
        transcript_data = json.load(file)
        
    return [entry["text"] for entry in transcript_data]

def save_text_to_json(text_entries, output_filename):
    with open(output_filename, 'w') as file:
        json.dump({"raw_text": text_entries}, file)

# Extract text entries from transcript.json
filename = "./output/transcript.json"
text_entries = extract_text_from_transcript_file(filename)

# Save the extracted text to raw_transcript.json
output_filename = "./output/raw_transcript.json"
save_text_to_json(text_entries, output_filename)
