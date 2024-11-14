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


source_path = r'C:\Users\lukes\Downloads'
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


    def move_file_by_type(self,src_path):
        # get name & type of file
        file_name = os.path.basename(src_path)
        file_type = src_path.split('.')[-1].lower()
        dst_path = None

        # find correct file type
        if file_type in video_type:
            dst_path = video_path
        elif file_type in audio_type:
            dst_path = audio_path
        elif file_type in image_type:
            dst_path = image_path       
        elif file_type in archive_type:
            dst_path = archive_path
        elif file_type in text_based_type:
            dst_path = text_based_path
        elif file_type in executable_type:
            dst_path = executable_path
        elif file_type in code_type:
            dst_path = code_path       

        # verify path exists,
        # * can also use "if os.path.exists(dst_path): "

        if dst_path and self.verify_file(dst_path) :
            dst = os.path.join(dst_path,file_name)
            try:
                shutil.move(src_path, dst)   
            except Exception as e:
                logging.error(f"Error occurred while moving file {file_name} : {e}")
     
        
    def on_modified(self, event):
        self.move_file_by_type(event.src_path)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    

    event_handler = downloadHandler()
    # organize (once) all files in source directory
    file_names = os.listdir(source_path)
    

    for name in file_names:
        file_path = os.path.join(source_path,name)
        if os.path.isfile(file_path):
            event_handler.move_file_by_type(file_path)
    
    
    observer = Observer(timeout=5)
    observer.schedule(event_handler, source_path)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt,SystemExit):
        observer.stop()
    observer.join()
    sys.exit(0)





