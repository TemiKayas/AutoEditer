import openai
import json
import re

#openai.api_key = "API KEY"
API_KEY=open("API_KEYS.env", "r")
openai.api_key = API_KEY.read()  # Replace with your API key

with open("./temp/output_audio.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="srt",
        language="en"
    )

print("Transcript generated")

def convert_transcript_to_dict(transcript_text):
    lines = transcript_text.strip().split('\n')
    transcription_entries = []
    
    i = 0
    while i < len(lines):
        entry = {}
        entry["id"] = int(lines[i])
        
        # Extract start and end timestamps
        time_info = lines[i + 1].split('-->')
        entry["start"] = time_info[0].strip()
        entry["end"] = time_info[1].strip()
        
        # Extract the text
        text_lines = []
        i += 2
        while i < len(lines) and lines[i].strip() != '':
            text_lines.append(lines[i])
            i += 1
        entry["text"] = ' '.join(text_lines)
        
        transcription_entries.append(entry)
        i += 1
        
    return transcription_entries

def save_transcript_to_json(transcript, filename):
    transcription_entries = convert_transcript_to_dict(transcript)

    with open(filename, 'w') as file:
        json.dump(transcription_entries, file)


save_transcript_to_json(transcript, './output/transcript.json')
