import tkinter as tk
import webbrowser


root = tk.Tk()
root.title("Technology Video")

root.geometry("700x450")


def video_open():
    webbrowser.open("https://www.youtube.com/shorts/nty3HC4N3-g?feature=share")


btn = tk.Button(
    root,
    text="Watch video ",
    command=video_open,
    font=("Arial", 12)
)

btn.pack(pady=20)


root.mainloop()