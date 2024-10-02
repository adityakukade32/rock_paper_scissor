import os

def createIfnotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(foldername,files):
    for file in files:
        os.replace(file,f"Media/{file}")
        
if __name__=="__main__":
        
    files=os.listdir()
    print(files)
    files.remove('main.py')
    createIfnotExist('Images')
    createIfnotExist('Media')
    createIfnotExist('Docs')
    createIfnotExist('Others')
    imgExts=[".png",".jpg",".jpeg"]
    images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]


    docExts=[".pdf",".txt",".docx",".doc"]
    docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]

    mediaExts=[".mp3",".mp4",".mkv",".mov"]
    media=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]



    others=[]
    for file in files:
    ext=os.path.splitext(file)[1].lower()
    if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)
        
        



    move("Media",media)
    move("Images",images)
    move("Docs",docs)
    move("Others",others)

    
   