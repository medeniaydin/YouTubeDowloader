import pytube
url = input("Enter video url: ")

path = ""
pytube.YouTube(url).streams.get_by_resolution(path).download(path)
