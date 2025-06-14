import os
import shutil
from tkinter import Tk, filedialog


# List of folder types to create
# types = ["images", "videos", "word", "audio", "txt", "pdf", "zip", "code"]

window = Tk()
window.withdraw()  # Hide the root cmd window


# Route to the directory you want to organize
# | route = r"C:\Users\Usuario\Downloads"  # r to avoid escape sequences
route = filedialog.askdirectory(
    title="Select the directory to organize"
)  # Open a dialog to select the directory


# Dictionary
extensions = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "PDFs",
    ".mp4": "videos",
    ".docx": "documents_word",
    ".txt": "documents_txt",
}

for folder in set(extensions.values()):
    folder_path = os.path.join(route, folder)
    print(f"Creating folder: {folder_path}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create each folder

for archive in os.listdir(route):  # List all files and folders in the directory
    route_archive = os.path.join(route, archive)  # match route with archive

    if os.path.isfile(route_archive):  # Check if it's a file
        name, ext = os.path.splitext(archive)  # Split the file name and extension
        ext = ext.lower()

        if ext in extensions:  # Check if the extension is in our dictionary
            destination_folder = os.path.join(route, extensions[ext], archive)
            shutil.move(route_archive, destination_folder)

print("Files organized successfully!")
