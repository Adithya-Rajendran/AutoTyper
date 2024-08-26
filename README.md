# TypeScript: Automatic File Typing Script

`TypeScript` is a Python-based utility that automatically types out the contents of a file using simulated keyboard input. This tool is ideal for pasting large amounts of text into web pages, remote desktop connections (RDP), or any other application where manual pasting might be cumbersome.

## Features

- **Automatic Typing:** Simulates keyboard typing of the contents of a specified file.
- **Custom Typing Delay:** Allows users to set a custom delay between each keystroke.
- **Typeable Character Validation:** The script checks for non-typeable characters before typing and exits if any are found, printing the first offending character.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## Installation

### Requirements

- Python 3.x
- `pyautogui` library

You can install the required library using pip:

```bash
pip install pyautogui
```

### Packaging as a Standalone Executable

To package the script as a standalone executable (so that users don't need to install Python or any libraries), use PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile type_script.py
```

The executable will be created in the dist directory.

## Usage

### Running the Script

To use the script, run it from the command line, specifying the file you want to type out:

```bash
python type_script.py <filename> [-t <typing_delay>]
```

 - `<filename>`: The name of the file whose contents you want to type out.
 - `-t <typing_delay>`: (Optional) The delay between each keystroke in seconds. Default is 0.05 seconds.

### Example

```bash
python type_script.py mytextfile.txt -t 0.1
```

This will type out the contents of mytextfile.txt with a 0.1-second delay between each keystroke.

## Handling Non-Typeable Characters

If the file contains non-typeable characters, the script will print an error message with the first offending character and exit.

Example output:

```bash
Error: Non-typeable character found: '�' (Unicode: 65533)
```
