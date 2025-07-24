# - Need to install LibreOffice on your Linux system
import os
from subprocess import run, PIPE  # Use subprocess to call libreoffice for conversion
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()  # Hide the root window

main_folder = filedialog.askdirectory(title="Select Folder with .docx Files")

destiny_folder = os.path.join(main_folder, "converted_PDFs")
os.makedirs(
    destiny_folder, exist_ok=True
)  # - Create destination folder if it doesn't exist

for archive in os.listdir(main_folder):
    if archive.endswith(".docx"):
        docx_path = os.path.join(main_folder, archive)
        command = [
            "soffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            destiny_folder,
            docx_path,
        ]
        run(command, stdout=PIPE, stderr=PIPE)
