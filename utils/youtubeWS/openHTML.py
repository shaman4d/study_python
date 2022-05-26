import webbrowser
import os
import pathlib

file_path = os.path.join(os.getcwd(), 'testYTvideo.html')
file_path_uri = pathlib.Path(file_path).as_uri()
webbrowser.open(file_path_uri)