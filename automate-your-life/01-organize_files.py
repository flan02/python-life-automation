import os
import shutil

# Route to the directory you want to organize
route = r"C:\Users\Usuario\Downloads"  # r to avoid escape sequences

# Create folders if they don't exist
types = ["images", "videos", "word", "audio", "txt", "pdf", "zip", "code"]

for type_ in types:
    folder_path = os.path.join(route, type_)
    print(f"Creating folder: {folder_path}")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)  # Create each folder

for archive in os.listdir(route):
    if archive.endswith(".jpg") or archive.endswith(".png"):
        shutil.move(
            os.path.join(route, archive), os.path.join(route, "images", archive)
        )
    elif archive.endswith(".mp4") or archive.endswith(".avi"):
        shutil.move(
            os.path.join(route, archive), os.path.join(route, "videos", archive)
        )
    elif archive.endswith(".docx") or archive.endswith(".doc"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "word", archive))
    elif archive.endswith(".wav") or archive.endswith(".mp3"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "audio", archive))
    elif archive.endswith(".txt"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "txt", archive))
    elif archive.endswith(".pdf"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "pdf", archive))
    elif archive.endswith(".zip"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "zip", archive))
    elif archive.endswith(".py"):
        shutil.move(os.path.join(route, archive), os.path.join(route, "code", archive))

print("Files organized successfully!")
