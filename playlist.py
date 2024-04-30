from pytube import YouTube, Playlist

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)

    # Loop through all videos in the playlist and download them
    for url in playlist.video_urls:
        youtube = YouTube(url)
        video = youtube.streams.get_by_itag(22)  # 720p video
        if video is not None:
            video.download(output_path='reactn')

# Use the function
download_playlist('https://www.youtube.com/playlist?list=PLC3y8-rFHvwhiQJD1di4eRVN30WWCXkg1')
