# Directory Organizer
This Python script helps organize files in a specified directory by sorting them into subfolders based on their file types.  
For example, video files, audio files, documents, and other file types will be moved to their respective folders.

## Why i wrote this script  


I have recently bought a new computer, and found myself downloading a large variety of files — installation programs, PDF's, ZIP files, and more.  
Before long, my Downloads folder became messy and unorganized, making it difficult to find what I needed.  
To solve this issue, i created this script to automatically organize any folder.     
This way, everything stays tidy, organized, and easy to find.

## Supported file types 
![image](https://github.com/user-attachments/assets/f92ab03c-b9d9-43d2-94de-49813052c46a)

here is the list of all currently supported file types and categories
## **Getting started**

### 1. Make sure you have [Python](https://www.python.org/downloads/) installed on your computer before starting!
### 2. Download required files
  ## Option 1 : Clone the repository (requires Git)

```
git clone https://github.com/lrobsky/directory-organizer.git
cd directory-organizer
```
  ## Option 2 :  Download the repository manually
- Click the green "Code" button at the top right corner of the repository, and select Download ZIP.
- Extract the downloaded .zip file to your desired location.


  
### 3. Installation 
- Open command prompt, and navigate to the cloned/extracted folder using:
  ```
  cd path\to\directory
  ```
  for example :
  ```
  cd C:\Users\lior\Desktop\directory-organizer
  ```
 - **Install dependencies** :  
    Inside the command prompt, write :
    ```
    pip install -r requirements.txt
    ```
- **Set up paths:**   
  Open the directoryOrganizer.py file and modify the paths to match your directories : 
    ```
    #Example
    source_path = r'C:\Users\lior\Downloads'
    video_path = r'C:\Users\lior\Desktop\Files\Video'
    ```
### 4. Running the script
- Inside the command prompt write :
```
python directoryOrganizer.py
```
- If you wish to stop the script, simply press **CTRL + C** or close the command prompt 


### 5. (Optional) Creating an .exe file and adding it to startup
If you want the script to run automatically every time your computer starts, follow these steps to convert the .py file into an .exe and add it to your startup.
- Create the .exe file  
Inside the command prompt write :
```
pyinstaller --onefile --noconsole directoryOrganizer
```
This will create an .exe file in your current directory

- Open the startup folder  
Press **Win + R** and into the box type :
```
shell:startup
```
This will open the startup folder on your computer.
- Copy&Paste the .exe file into the startup folder.
  
Now, the script will automatically launch every time your computer starts!




