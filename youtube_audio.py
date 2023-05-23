import pafy

url = "youtube_url"

video = pafy.new(url=url)
video_title = video.title

best_audio = video.getbestaudio()
best_audio.download()

print(video_title)

# urls = ['url_list']
# for url in urls:
#     video = pafy.new(url=url)
#     video_title = video.title
#
#     best_audio = video.getbestaudio()
#     best_audio.download()
#
#     print(video_title)
