import openai
import json
import re
openai.api_key = "PUT API KEY HERE"
"""
audio_file= open("./output_audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)
print("Transcription complete!")
print(transcript)
"""

with open("./output_audio.mp3", "rb") as audio_file:
    transcript = openai.Audio.transcribe(
        file = audio_file,
        model = "whisper-1",
        response_format="srt",
        language="en"
    )

print("Transcript generated")

#Pass a prompt to whisper to save as a json, begin testing with GPT intergation for that JSON. 



def extract_key_points(transcription: str) -> list:
    lines = transcription.split('\n')
    key_points_data = []

    i = 0
    while i < len(lines):
        if "-->" in lines[i]:
            time_stamp = lines[i]
            text = ""
            
            # iterate to gather multi-line texts
            j = i + 1
            while j < len(lines) and "-->" not in lines[j]:
                text += lines[j] + " "
                j += 1

            # Make API call to get key points from ChatGPT
            response = openai.Completion.create(
                engine="text-davinci-002",  # or your preferred engine
                prompt=f"Extract key points from the following text, then display those key points only using sentances pulled from the provided text:\n{text}",
                max_tokens=250
            )
            
            # Extract the key points returned by ChatGPT
            key_point = response.choices[0].text.strip()
            
            if key_point:
                key_points_data.append({
                    "time": time_stamp,
                    "text": key_point
                })

            i = j
        else:
            i += 1

    return key_points_data

# Example usage
transcription_str = transcript

key_points_data = extract_key_points(transcription_str)

# Save the extracted key points to a JSON file
with open('key_points.json', 'w') as json_file:
    json.dump(key_points_data, json_file, indent=4)
