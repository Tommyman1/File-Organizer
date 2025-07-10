# File Organizer Script 🗂️

This Python script allows you to organize files on your computer by categorizing them based on their extensions. It supports common types like images, videos, documents, executables, and more.

## ✅ Features

- Automatically detects the platform (Windows, macOS, Linux)
- Filters out system and hidden folders
- Organizes files by extension into pre-defined categories
- Creates new folders for unknown file types
- Handles duplicate filenames by renaming with a counter
- Allows recursive folder selection for deep organization

## 📂 File Categories

- Images (`.jpg`, `.png`, `.gif`, etc.)
- Videos (`.mp4`, `.avi`, etc.)
- Audio (`.mp3`, `.wav`, etc.)
- Documents, Spreadsheets, Presentations
- Text files, Scripts, Archives, Executables
- Other folders for anything uncategorized

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal or command prompt.
3. Navigate to the script's directory.
4. Run:

```bash
python file_organizer.py


NOTES

-Files in hidden/system folders are ignored.

-If a file with the same name exists in the destination, it will be renamed to avoid overwriting.

-Only local user folders are scanned (e.g., C:\Users\ on Windows).

No external libraries required — uses only Python standard library.