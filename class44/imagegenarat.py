import tkinter as tk
import requests

url=""
api=""

def generate_image():
    text=prompt_entry.get()
    params={"q":text,"appid":api,"units":"metric"}
    res=requests.get(url,params=params,timeout=8)
    
    


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
