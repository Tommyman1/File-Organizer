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

Images & Graphics: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .webp, .svg, .heic, .ico, .pdf, .avif

Videos: .mp4, .mkv, .avi, .mov, .wmv, .flv, .webm, .3gp, .mpeg, .m4v

Audio: .mp3, .wav, .flac, .aac, .ogg, .wma, .m4a, .opus, .alac

Work Files (Documents, Spreadsheets, Presentations):
.doc, .docx, .odt, .rtf, .pdf, .tex, .xls, .xlsx, .ods, .csv, .tsv, .ppt, .pptx, .odp, .key, .pps

Text Files: .txt, .md, .log, .ini, .cfg, .epub

Executables & Installers: .exe, .msi, .sh, .bat, .app, .apk, .deb, .rpm, .bin, .command

Compressed Archives: .zip, .rar, .7z, .tar, .gz, .bz2, .xz, .iso, .dmg

Code & Scripts: .py, .js, .ts, .jsx, .tsx, .java, .c, .cpp, .h, .cs, .html, .css, .json, .xml, .yml, .yaml, .php, .rb, .go, .rs, .sql, .ipynb, .wpress

Games (ROMs, saves, emulator formats, mods):
Save files: .sav, .srm, .dat, .bin, .rpf
Extended saves: .sav1 to .sav12, .sa1 to .sa12
Cheat files: .cheats
Save snapshots: .ss1 to .ss9
Mods & packages: .pak, .wad, .vpk, .xci
ROMs & disc images: .iso, .img, .cia, .nds, .3ds, .nsp, .wbfs, .gcm
Emulator formats: .gba, .gb, .gbc, .nes, .smc, .sfc, .n64, .z64, .cue, .gdi, .cdi, .d64, .prg, .a26, .fds

Other folders: For uncategorized or miscellaneous folders

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
