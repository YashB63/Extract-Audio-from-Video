from moviepy.editor import *

#25 second ka video
# clip_one = VideoFileClip("Enter the file path of video(in our case "test_one.mp3")").subclip(0, 25)
# #clip_one.audio.write_audiofile("test_one.mp3")
# clip_one = clip_one.without_audio()
# clip_one.write_videofile("test_vid_one.mp4")

# video_file = VideoFileClip("test_vid_one.mp4")
# audio_file = AudioFileClip("Enter the path of audio you want to add on video")

# final_video = video_file.set_audio(audio_file)
# final_video.write_videofile("test_new_one.mp4")

#Doing both steps in a single function

#25 second ka video
main_video = VideoFileClip("Enter the path of the video").subclip(10,35)
main_video = main_video.without_audio()

main_audio = AudioFileClip("Enter the path of the audio you want to add")
final_video = main_video.set_audio(main_audio)
final_video.write_videofile("finalvideo.mp4")
