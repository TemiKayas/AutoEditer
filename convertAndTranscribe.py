from moviepy.editor import *
import openai

def convert_video_to_audio(video_path, audio_path):
    """
    Convert a video file to an audio file.

    Parameters:
    - video_path (str): Path to the input video file.
    - audio_path (str): Path to save the output audio file.
    """
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, codec='mp3')
    print(f"Video converted to audio! Saved at {audio_path}")

# Example usage:
video_path = "./transcribetest.mp4"
audio_path = "./output_audio.mp3"
convert_video_to_audio(video_path, audio_path)
