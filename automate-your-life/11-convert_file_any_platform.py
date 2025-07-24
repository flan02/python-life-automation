import os
import platform
import subprocess
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()  # Hide the root window

main_folder = filedialog.askdirectory(title="Select Folder with .docx Files")

destiny_folder = os.path.join(main_folder, "converted_PDFs")
os.makedirs(
    destiny_folder, exist_ok=True
)  # - Create destination folder if it doesn't exist

system = platform.system()  # $ Get the operating system type


def convert_libreoffice(docx_path):
    command = [
        "soffice",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        destiny_folder,
        docx_path,
    ]
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def convert_docx2pdf(docx_path, pdf_path):
    from docx2pdf import convert  # Transform .docx files to PDF

    convert(docx_path, pdf_path)


for archive in os.listdir(main_folder):
    if archive.endswith(".docx"):
        docx_path = os.path.join(main_folder, archive)
        pdf_path = os.path.join(destiny_folder, archive.replace(".docx", ".pdf"))

        if system == "Windows":
            try:
                convert_docx2pdf(docx_path, pdf_path)
            except Exception as e:
                print(f"Failed to convert {archive} using docx2pdf: {e}")
        elif system == "Linux":
            convert_libreoffice(docx_path)

print(f"Converted {archive} to PDF.")
