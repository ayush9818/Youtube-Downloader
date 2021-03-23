from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube



Folder_Name = ""
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose Folder!",fg="red")


def choose_resolution(resolution):
    if resolution == "360p":
        itag=18
    elif resolution == "720p":
        itag=22
    elif resolution == "1080p":
        itag=137
    elif resolution == "4K":
        itag=313
    else:
        itag = -1

    return itag

def download_video():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if len(url) > 1:
        ytdError.config(text="")
        itag = choose_resolution(choice)

        if itag == -1:
            ytdError.config(text="Paste Link Again!",fg="red")

        else:
            video=YouTube(url)
            #stream = yt.streams.filter(file_extension='mp4')

            print(itag)

            try:
                stream = video.streams.get_by_itag(itag)
                #stream.default_filename
                stream.download(Folder_Name)
                ytdError.config(text="Download Completed",fg="red")
            except:
                ytdError.config(text="Resolution Not Available",fg="red")





root = Tk()
root.title("Youtube Downloader")
root.geometry("350x400")
root.columnconfigure(0, weight=1) # set content in center



ytdLabel = Label(root, text="Enter the URL of the Video",font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

ytdError = Label(root, text="Error Message", fg='red', font=("jost",15))
ytdError.grid()

saveLabel = Label(root,text="Save Video File",font=("jost",15,'bold'))
saveLabel.grid()

saveButton = Button(root,width=10,bg='red',fg='white',text="Choose Path",command=openLocation)
saveButton.grid()

locationError = Label(root,text="Error Message of Path", fg="red", font=("jost",15))
locationError.grid()

ytdQuality = Label(root,text="Select Quality",font=("jost",15))
ytdQuality.grid()

choices=['360p','720p','1080p','4K']
ytdChoices=ttk.Combobox(root,values=choices)
ytdChoices.grid()

downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",font=("jost",15),command=download_video)
downloadbtn.grid()

root.mainloop()
