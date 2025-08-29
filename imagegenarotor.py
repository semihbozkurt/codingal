import tkinter as tk
import requests
from PIL import Image , ImageTk
from tkinter import messagebox
from io import BytesIO

url="https://clipdrop-api.co/text-to-image/v1"
api="f55876c72b9198d417f033d9c2b53ada594d60770a3699f5a6846f90639d4d7fb038ef8ca2c33e8eea8e31c3c2982107"

def generate_image():
    text=prompt_entry.get().strip()
    if text=="":
        messagebox.showwarning("warning","please write something")
        return
    status_label.config(text="image is getting genarated",fg="blue")
    root.update()
    try:
       
        
        
        res=requests.post(url,files= {
            "prompt":(None,text,"text/plain")} , headers={"x-api-key":api})
        
        if res.ok:
            print(res.content)

            imgdata=BytesIO(res.content)
            img= Image.open(imgdata)

            maxwidth=512
            maxheigth=512
            if img.height>maxheigth or img.width>maxwidth:
                img=img.resize((maxheigth,maxwidth),Image.LANCZOS)
            imagetk= ImageTk.PhotoImage(img)
            image_label.config(image=imagetk)
            image_label.image=imagetk
            status_label.config(text="DONE",fg="green")
        else: 
            res.raise_for_status()
    except Exception as e:
        status_label.config(text="error occured"+str(e),fg="red")

    


root = tk.Tk()
root.title("AI Image Generator")
root.geometry("600x700")

# Prompt Input
tk.Label(root, text="Enter your prompt:", font=("Arial", 12)).pack(pady=10)
prompt_entry = tk.Entry(root, width=60, font=("Arial", 11))
prompt_entry.insert(0, "Shot of vaporwave fashion dog in Miami")
prompt_entry.pack(pady=5)

# Generate Button
generate_button = tk.Button(root,
                            text="Generate Image",
                            command=generate_image,
                            font=("Arial", 12))
generate_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="blue", font=("Arial", 10))
status_label.pack(pady=5)

# Image Display Frame
image_label = tk.Label(root)
image_label.pack(pady=15)

root.mainloop()
