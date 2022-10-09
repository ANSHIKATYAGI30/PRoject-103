import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/ANSHIKA TYAGI/Desktop'

class fileEventHandler (FileSystemEventHandler):
    def on_created(self, event):
        print(f'Heyy!, {event.src_path} has been created.')
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")
    def on_modified(self, event):
        print(f"Oh, It seems as if someone modified{event.src_path}")
    def on_moved(self, event):
        print(f"Someone moved{event.src_path}") 

event_handler = fileEventHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive= True)
observer.start()
try: 
 while True :
    time.sleep(2)
    print('Running!!')
except KeyboardInterrupt:
    print('Stopped!!')
    observer.stop() 
