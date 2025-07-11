import os

# import stat  # To change file permissions (if needed)
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


def select_folder():
    """Open a dialog to select a folder."""
    folder = filedialog.askdirectory()
    if folder:
        folder_entry.delete(0, tk.END)  # Clear the entry field
        folder_entry.insert(0, folder)  # Insert the selected folder path


def rename_files():
    """Rename files in the selected folder with a specified prefix and extension."""
    folder = folder_entry.get()  # Get the folder path from the entry field
    prefix = prefix_entry.get()  # Get the prefix from the entry field
    ext = tuple(ext_entry.get().split(","))  # ? Convert list of extensions to a tuple

    archives = []  # empty list

    for f in os.listdir(folder):
        if f.endswith(ext):
            archives.append(f)

    # Create a file to revert the changes
    route_revert = os.path.join(folder, "revert_changes.bat")
    with open(route_revert, "w", encoding="utf-8") as revert_file:
        for i, current_name in enumerate(archives, start=1):
            current_ext = os.path.splitext(current_name)[1]  # Get the file extension
            new_name = (
                f"{prefix}{i:03}{current_ext}"  # Format the number with leading zeros
            )
            old_path = os.path.join(folder, current_name)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)  # Rename the file
            print(
                f"Renamed '{current_name}' to '{new_name}'"
            )  # image_001.jpg, image_002.png, etc.
            revert_file.write(
                f'rename "{new_path}" "{current_name}"\n'
            )  # Write the revert command
        revert_file.write('del "%~f0"\n')  # - Delete the revert file itself

    # print(f"Revert completed. Execute the .bat file to revert changes '{route_revert}'")
    messagebox.showinfo(
        "Success", f"Files renamed successfully!\nRevert file created: {route_revert}"
    )


# --------------------- USER INTERFACE ---------------------

window = tk.Tk()
window.title("File Renamer")
window.geometry("400x250")
window.resizable(False, False)  # nor width nor height can be changed

tk.Label(window, text="File Renamer", font=("Arial", 16)).pack(pady=10)

frame_folder = tk.Frame(window)
frame_folder.pack()

folder_entry = tk.Entry(frame_folder, width=40)
folder_entry.pack(side=tk.LEFT, padx=5)
tk.Button(frame_folder, text="Browse", command=select_folder).pack(side=tk.LEFT)

tk.Label(window, text="Files' prefix:").pack(pady=5)
prefix_entry = tk.Entry(window, width=20)
prefix_entry.insert(0, "image_")  # Default prefix
prefix_entry.pack()

tk.Label(window, text="Ext (separate by comma):").pack(pady=5)
ext_entry = tk.Entry(window, width=20)
ext_entry.insert(0, ".jpg, .png")  # Default prefix
ext_entry.pack()

tk.Button(
    window, text="Rename Files", command=rename_files, bg="#04ba04", fg="white", padx=10
).pack(pady=10)

window.mainloop()  # Start the GUI event loop
