import moviepy
from moviepy import VideoFileClip, TextClip
from pathlib import Path

# audio will inherit the name of the video
video_file = Path("the_name_of_the_video.mp4")
video = moviepy.VideoFileClip(f"{video_file}")
audio = video.audio
audio.write_audiofile((f{"video_file.stem}).mp3")

# Cleanup
video.close()
audio.close()
print("✅ Done! Check my_audio.mp3")
