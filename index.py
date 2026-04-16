import moviepy
from moviepy import VideoFileClip, TextClip

video = moviepy.VideoFileClip("name of you file.mp4")
audio = video.audio
audio.write_audiofile("my_audio.mp3")

# Cleanup
video.close()
audio.close()
print("✅ Done! Check my_audio.mp3")
