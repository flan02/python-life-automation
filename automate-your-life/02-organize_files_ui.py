import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


# Dictionary with file extensions for each type
EXTENSIONS = {
    "images": [".jpg", ".png"],
    "videos": [".mp4", ".avi"],
    "word": [".docx", ".doc"],
    "audio": [".mp3", ".wav"],
    "txt": [".txt"],
    "pdf": [".pdf"],
    "zip": [".zip"],
    "code": [".py", ".js", ".tsx", ".css", ".ts"],
}

# Dictionary with control var for checkboxes
check_vars = {}


# Función que organiza los archivos
def organize_archives(ruote):
    if not ruote:
        messagebox.showwarning("Error", "You must add a route")
        return

    selected = [type for type, var in check_vars.items() if var.get()]

    if not selected:
        messagebox.showwarning(
            "Error", "You must select at least one folder/type to organize"
        )
        return

    # Create folder if checked was selected
    for type in selected:
        folder = os.path.join(ruote, type)
        if not os.path.exists(folder):
            os.makedirs(folder)
        else:
            messagebox.showwarning("Error", f"The folder {folder} already exists")

    # Move archives to their respective folders
    for archive in os.listdir(ruote):
        archive_path = os.path.join(ruote, archive)
        if os.path.isfile(archive_path):
            for type in selected:
                extensiones = EXTENSIONS[type]
                if any(archive.lower().endswith(ext) for ext in extensiones):
                    destiny = os.path.join(ruote, type, archive)
                    if not os.path.exists(destiny):
                        if copy_files_var.get():
                            shutil.copy2(
                                archive_path, destiny
                            )  # TODO: copy instead of move [copy2 keeps metadata]
                        else:
                            shutil.move(archive_path, destiny)
                    break  # is matched, no need to check further

    messagebox.showinfo("Success", "Archives organized!!!")  # (title, message)


# Fc to select a folder
def select_folder():
    route = filedialog.askdirectory()
    if route:
        entry_route.delete(0, tk.END)
        entry_route.insert(0, route)


def toggle_all_checkboxes():
    state = select_all_var.get()
    for var in check_vars.values():
        var.set(state)


# $ UI setup
root = tk.Tk()
root.title("Archive Organizer")
copy_files_var = tk.BooleanVar()
# This var is user to select/deselect all checkboxes
select_all_var = tk.BooleanVar()
# Field route
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Folder route:").grid(row=0, column=0, sticky="w")
entry_route = tk.Entry(frame, width=50)
entry_route.grid(row=1, column=0, padx=(0, 10))

btn_explore = tk.Button(frame, text="Find...", command=select_folder)
btn_explore.grid(row=1, column=1)

frame_check = tk.LabelFrame(root, text="Select types to organize", padx=10, pady=10)
frame_check.pack(padx=10, pady=10)

row = 2
tk.Checkbutton(
    frame_check,
    text="Only copy files",
    variable=copy_files_var,
    command=toggle_all_checkboxes,
).grid(row=0, column=0, sticky="w")
tk.Checkbutton(
    frame_check,
    text="Select/Deselect All",
    variable=select_all_var,
    command=toggle_all_checkboxes,
).grid(row=1, column=0, sticky="w")
for type in EXTENSIONS:
    var = tk.BooleanVar(value=True)  # Default to True
    check_vars[type] = var
    tk.Checkbutton(
        frame_check,
        text=f"{type.capitalize()} ({', '.join(EXTENSIONS[type])})",
        variable=var,
    ).grid(row=row, column=0, sticky="w")
    row += 1

btn_organize = tk.Button(
    root, text="Organize archives", command=lambda: organize_archives(entry_route.get())
)
btn_organize.pack(pady=10)

root.mainloop()
