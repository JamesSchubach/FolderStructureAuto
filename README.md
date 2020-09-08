# Automated Folder Structure Script
FolderStructureAuto is a script that automates the process of moving files into seperate folders, with this script
all you need to do is run it, move a file into said folder and it will reorganise the whole folder into
new subfolders. Right now the subfolders are images, videos, zip, exe, documents, html, music and misc.

## Requirements 
This script will only run on python3
Please install watchdog via the following command before running the script

```bash
pip install watchdog
```

## Usage

To run the script, it is a simple as typing this command where the script is located.
FOLDER_PATH: Represents the path to which folder you want organised.
i.e: C:\Users\schub\Downloads
<br>
**Important do not have script in the folder you are trying to reorganize**
```bash
python3 folder_structure_auto.py FOLDER_PATH
```
To exit, press Ctrl+c to stop the script from running

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
