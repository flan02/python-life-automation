import os
import shutil
import getpass  # To get the username of the current user
from tkinter import Tk, filedialog
from datetime import datetime

user = getpass.getuser()  # Get the current user's username

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
            # Create the destination folder based on the extension
            # | destination_folder = os.path.join(route, extensions[ext], archive)

            # Let's implement subfolders for each file's date
            date_modified = datetime.fromtimestamp(os.path.getmtime(route_archive))
            # print("We get a timestamp", date_modified)
            date_subfolder = date_modified.strftime("%Y-%m")  # Format: YYYY-MM

            folder_type = os.path.join(route, extensions[ext])
            folder_date = os.path.join(
                folder_type, date_subfolder
            )  # match folder type with date
            if not os.path.exists(folder_date):
                os.makedirs(folder_date)
            destination_folder = os.path.join(folder_date, archive)
            shutil.move(route_archive, destination_folder)
            with open(os.path.join(route, "log.txt"), "a", encoding="utf-8") as log:
                log.write(
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - User: {user} - Moved: {archive} -> {destination_folder}\n"
                )

print("Files organized successfully!")
