import openai
import chardet

API_KEY = 'openai-api-key'
model_id = 'whisper-1'
language = "en"
# audio_file_path = '/content/drive/MyDrive/audio/output.mp3'
audio_file = open("media/output.mp3", 'rb')

response = openai.Audio.transcribe(
    api_key=API_KEY,
    model=model_id,
    file=audio_file,
    language='en'
)


def transcribe_audio():
    transcription_text = response.text

    # Specify the path and filename for the text file
    output_file = "media/transcription.txt"

    # Write the transcription text to the file
    with open(output_file, "w") as file:
        file.write(transcription_text)

    print("Transcription saved to:", output_file)

# import assemblyai as aai
#
# aai.settings.api_key = "05c45b6bf84f42208af5857abed4308a"
# transcriber = aai.Transcriber()
#
# transcript = transcriber.transcribe("media/output.mp3")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")
#
# text = transcript.text
#
# # Save the transcript as a text file
# output_file = 'media/transcript_aai.txt'
# with open(output_file, 'w') as file:
#     file.write(text)
#
# print("Transcription:", text)
# print("Transcript saved as:", output_file)


# OPENAI WHISPER

# from pytube import YouTube
#
# video_url = "https://www.youtube.com/watch?v=v6OB80Vt1Dk&t=1s&ab_channel=KevinStratvert"
#
# yt = YouTube(video_url)
# stream = yt.streams.get_highest_resolution()
# stream.download()
