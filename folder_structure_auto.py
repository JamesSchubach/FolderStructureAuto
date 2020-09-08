import os
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            path = os.path.join(folder_to_track, filename)
            if path in paths.values():
                continue
            ext = filename.rpartition('.')[-1].lower()
            ext = '.'+ext
            src = folder_to_track + "/" + filename
            if ext in ['.jpg', '.jpeg', '.png', '.gif', 'webp', '.tiff', '.psd', '.raw', '.bmp', '.heif', '.indd']:
                new_destination = paths['images'] + "/" + filename
            elif ext in [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".m4p", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv"]:
                new_destination = paths['videos'] + "/" + filename
            elif ext in [".zip", ".rar", ".7z", ".gz", '.7zip']:
                new_destination = paths['zip'] + "/" + filename
            elif ext in [".exe", ".app", ".vb", ".scr", '.bat']:
                new_destination = paths['exe'] + "/" + filename
            elif ext in [".pdf", ".txt", ".doc", ".docx", '.xls', '.xlsx', '.ppt', '.pptx']:
                new_destination = paths['documents'] + "/" + filename
            elif ext in [".html"]:
                new_destination = paths['html'] + "/" + filename
            elif ext in [".aac", ".wma", ".wav", '.mp3', '.flac', '.m4a']:
                new_destination = paths['music'] + "/" + filename
            else:
                new_destination = paths['misc'] + "/" + filename
            os.rename(src, new_destination)


folder_to_track = sys.argv[1]
if not os.path.isdir(folder_to_track):
    print("This Folder does not exist")
    raise SystemExit

paths = {
    "images": os.path.join(folder_to_track, "images"),
    "videos": os.path.join(folder_to_track, "videos"),
    "zip": os.path.join(folder_to_track, "zip"),
    "exe": os.path.join(folder_to_track, "exe"),
    "documents": os.path.join(folder_to_track, "documents"),
    "html": os.path.join(folder_to_track, "html"),
    "music": os.path.join(folder_to_track, "music"),
    "misc": os.path.join(folder_to_track, "misc")
}
for newpath in paths.values():
    if not os.path.isdir(newpath):
        os.makedirs(newpath)
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
