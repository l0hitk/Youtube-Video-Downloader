from tkinter import Tk, Label, Entry, Button, filedialog, OptionMenu, StringVar
from pytube import YouTube

def download_video():
    try:
        url = YouTube(str(link.get()))
        video = url.streams

        resolutions = [stream.resolution for stream in video.filter(progressive=True).order_by('resolution')]

        resolutions = [res for res in resolutions if res in ['720p', '1080p']]

        resolution_var = StringVar(root)
        resolution_var.set(resolutions[0])

        resolution_menu = OptionMenu(root, resolution_var, *resolutions)
        resolution_menu.place(x=180, y=180)

        output_directory = filedialog.askdirectory()

        video.get_by_resolution(resolution_var.get()).download(output_directory)

        Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)
    except Exception as e:
        Label(root, text='ERROR: ' + str(e), font='arial 15').place(x=180, y=210)

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Python-based YouTube Video Downloader")

Label(root, text='YouTube Video Downloader', font='arial 20 bold').pack()

link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=download_video).place(x=180, y=150)

root.mainloop()