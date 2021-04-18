from moviepy.editor import VideoFileClip, clips_array

game = VideoFileClip("myvideo.mp4")  # add 10px contour
statistic = VideoFileClip("myvideo1.mp4")
final_clip = clips_array([[game, statistic]])
final_clip.audio = final_clip.audio.set_fps(game.audio.fps)  # без нее ничего не работает хз почему
final_clip.preview(fps=game.fps)
final_clip.write_videofile("my_stack.mp4", threads=8) # нужно понять что значат эти потоки, а также желательно подключиьт многопоточность и асинхронность
