from moviepy.editor import VideoFileClip

# Provide the path to your video file
video_file = "input/video.mp4"

# Provide the desired output path for the MP3 file
output_file = "media/output.mp3"


def extract_audio_from_video():
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file, codec='mp3')
