from abstractive_summery import t5_summary
from headline import t5_headline
from extract_audio import extract_audio_from_video

# Call the function to extract audio from the video
from save_pdf import create_pdf

extract_audio_from_video()

from whisper import transcribe_audio

# transcribe audio file using openai whisper pretrained model
transcribe_audio()

# generate summary article using generated transcription
file_path = "media/transcription.txt"
# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    transcription = file.read()

generated_summary = t5_summary(transcription)

# Print the generated summary
print("Final Generated Summary:", generated_summary)

# generate headline using generated summary
file_path = "media/summary.txt"
# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    text2headline = file.read()
generated_headline = t5_headline(text2headline)
# Print the generated summary
print("Final Generated Headline:", generated_headline)

output_file = "media/final_output.pdf"
create_pdf(output_file, transcription, generated_summary, generated_headline)


