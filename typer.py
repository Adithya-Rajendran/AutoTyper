import sys
import pyautogui
import time
import argparse
import string

def type_file_content(filename, delay):
    try:
        typeable_chars = set(string.printable)
        
        with open(filename, 'r') as file:
            content = file.read()

            for char in content:
                if char not in typeable_chars:
                    print(f"Error: Non-typeable character found: '{char}' (Unicode: {ord(char)})")
                    sys.exit(1)


        time.sleep(delay)

        print(content)
        pyautogui.write(content, interval=0.05)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Automatically type out the contents of a file.")
    parser.add_argument("filename", help="The name of the file to type out.")
    parser.add_argument("-t", "--time", type=float, default=5.00, 
                        help="Delay in seconds before starting to type.")

    args = parser.parse_args()

    type_file_content(args.filename, args.time)

if __name__ == "__main__":
    main()
