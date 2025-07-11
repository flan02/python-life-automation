# .bat for windows and .sh for linux

import os
# import stat  # To change file permissions (if needed)

folder = r"C:\Users\Usuario\Downloads"
prefix = "image_"
ext = (".jpg", ".png")  # Tuple

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


print(f"Revert completed. Execute the .bat file to revert changes '{route_revert}'")
