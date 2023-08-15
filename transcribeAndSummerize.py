import openai
import json
import re
openai.api_key = "API KEY"


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

            # This is the GPT API Call, still needs a bunch of work until the summery function is valiable
            response = openai.Completion.create(
                engine="text-davinci-002",  # or your preferred engine
                prompt=f"Your job is to help automatically edit videos, to do this you will take a transcript provided from another method, then  you will Extract key points from the transcript, creating a summary. Once your summary has been created, you will take direct quotes from the transcript and stich them together in order to express your summary using only direct quotes. Please pass the summary expressed in direct quotes along with the time stamps into a JSON file format. Here is transcript I would like you to use:\n{text}",
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

with open('transcript.json', 'w') as json_file:
    json.dump(transcript, json_file, indent=4)


"""
key_points_data = extract_key_points(transcription_str)

# Save the extracted key points to a JSON file
with open('key_points.json', 'w') as json_file:
    json.dump(key_points_data, json_file, indent=4)
"""
# ^ Is the mothod for making the summery call and saving to JSON