import os
import shutil
import getpass  # To get the username of the current user
import time  # Handle time-related tasks
from tkinter import Tk, filedialog
from datetime import datetime
from watchdog.observers import Observer  # Monitor file system events
from watchdog.events import FileSystemEventHandler  # Respond to file system events

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


def wait_for_file(
    route_file, tries=10, timeout=0.5
):  # Gives 5 seconds to the file to be created
    for _ in range(tries):
        try:
            with open(route_file, "rb"):
                return True  # File is accessible
        except (PermissionError, OSError):
            time.sleep(timeout)  # Wait before retrying

    return False


def order_files(route):
    for archive in os.listdir(route):  # List all files and folders in the directory
        route_archive = os.path.join(route, archive)  # match route with archive

        if (
            os.path.isfile(route_archive) and archive != "log.txt"
        ):  # Check if it's a file / exclude log.txt
            if not wait_for_file(route_archive):
                print(f"File {archive} is not accessible after waiting.")
                continue  # skip to the next file
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


# - Create class to build the file observer
class EventHandler(FileSystemEventHandler):
    def on_created(
        self, event
    ):  # watchdog library calls automatically this method when a file is created
        if not event.is_directory:  # Check if the event is for a file
            print(f"New file detected: {event.src_path}")
            order_files(route)  # Organize files. Fc must be defined before this class


for folder in set(extensions.values()):
    folder_path = os.path.join(route, folder)
    print(f"Creating folder: {folder_path}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create each folder

order_files(route)  # Initial call to organize existing files


# - Create the observer
event_handler = EventHandler()  # Create an instance of the event handler
observer = (
    Observer()
)  # Create an observer instance. Monitor file system events for changes
observer.schedule(
    event_handler, route, recursive=False
)  # 3rd params in true to monitor subfolders
observer.start()  # Start the observer (it will run in a separate thread)

print(f"Monitoring directory: {route}")
print("Press Ctrl+C to stop the observer.")

try:
    while True:
        time.sleep(1)  # Keep the script running
except KeyboardInterrupt:
    print("Stopping observer...")
    observer.stop()

observer.join()  # Wait for the observer to finish
