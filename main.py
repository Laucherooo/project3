import os, sys
import time
import csv
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_modified(self, event):
        path = 'result/log.txt'
        f = open(path, 'w')
        f.write(f"{datetime.now()}-- File: {event.src_path} has been modified.\n")
        f.close()
        print(f"hey, {event.src_path} has been modified!")

        if not event.is_directory:
            path = os.path.realpath(event.src_path)
            print("Modified file's name> {0}".format(path))
            ext = os.path.splitext(path)[1]
            if ext == '.txt':
                txt = open(path).read()
                print("File content>")
                print(txt)
            if ext == '.csv':
                file = open(path)
                reader = csv.DictReader(file, ['username', 'Id', 'first_name', 'last_name'])
                for row in reader:
                    print(row['username'], row['Id'], row['first_name'],row['last_name'])
                file.close()

    def on_created(self, event):
        path = 'result/log.txt'
        f = open(path, 'w')
        f.write(f"{datetime.now()}-- File: {event.src_path} has been created.\n")
        f.close()
        print(f"hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        path = 'result/log.txt'
        f = open(path, 'w')
        f.write(f"{datetime.now()}-- File: {event.src_path} has been deleted.\n")
        f.close()
        print(f"Someone deleted {event.src_path}!")

    def on_moved(self,event):
        path = 'result/log.txt'
        f = open(path, 'w')
        f.write(f"{datetime.now()}-- File: {event.src_path} has been moved to {event.dest_path}.\n")
        f.close()
        print(f"Someone moved {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print('watching the file：%s' % os.path.realpath(path))
    print('Ctrl-C to quit!')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

"""
if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    print(f"hey, {event.src_path} has been created!")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved

path = "result"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
       time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
"""
