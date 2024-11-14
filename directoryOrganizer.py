import os
import sys
import time
import logging
import shutil
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler




# file types by category


video_type = {"mp4", "mkv", "mov", "avi", "flv", "wmv" }
audio_type = {"mp3", "wav", "aac", "flac", "ogg"}
image_type = {"png","jpg","jpeg"}
archive_type = {"zip","rar","7z","tar","gz"}
text_based_type = {"pdf","txt","doc","docx","xls","csv","xlsx","pptx","ppt","md","epub","mobi"}
executable_type = {"exe","bat","msi"}
code_type  = {"py","cpp","java","c","html","css","js","xml","php","json","jsonl","yaml"}


# paths
# 
# 


download_path = r'C:\Users\lukes\Downloads'
video_path = r'C:\Users\lukes\Desktop\Files\Video'
audio_path = r'C:\Users\lukes\Desktop\Files\Audio'
image_path = None
archive_path = None
text_based_path = None
executable_path = None
code_path = None




class downloadHandler(LoggingEventHandler):
    
    def verify_file(self,src,time_limit = 30):
        verified = False
        time_waited = 0
        previous_size = os.path.getsize(src)

        while time_waited < time_limit and not verified:
            time.sleep(1)
            current_size = os.path.getsize(src)
            if current_size == previous_size:
                verified = True
            else:
                previous_size = current_size
            time_waited+=1        

        return verified    

    def on_modified(self, event):
        time.sleep(2)
        # get name & type
        file_name = event.src_path.split('\\')[-1]
        file_type = event.src_path.split('.')[-1].lower()
        path = None

    # find correct file type
        if file_type in video_type:
            path = video_path
        elif file_type in audio_type:
            path = audio_path
        elif file_type in image_type:
            path = image_path       
        elif file_type in archive_type:
            path = archive_path
        elif file_type in text_based_type:
            path = text_based_path
        elif file_type in executable_type:
            path = executable_path
        elif file_type in code_type:
            path = code_path       

# verify path exists,
# * can also use if os.path.exists(path)

        if path and self.verify_file(path) :
            dst = os.path.join(path,file_name)
            shutil.move(event.src_path, dst)        
        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = downloadHandler()
    observer = Observer()
    observer.schedule(event_handler, download_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()





