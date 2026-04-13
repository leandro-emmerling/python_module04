#!/usr/bin/env python3


import sys
import typing


def transform_content(content: str) -> str:
    lines: list[str] = content.split("\n")
    new_lines: list[str] = []
    for line in lines:
        if line:
            line += "#"
        new_lines.append(line)
    return "\n".join(new_lines)


def main() -> None:
    """Run the main Program."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file: typing.IO[str] | None = None
    file_content: str = ""
    try:
        file = open(sys.argv[1], "r")
        print("---\n")
        file_content = file.read()
        print(file_content)
        print("---")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")
    if file_content:
        new_content: str = transform_content(file_content)
        print("\nTransform data:")
        print("---\n")
        print(new_content)
        print("---")
        new_filename: str = input("Enter new file name (or empty): ")
        if not new_filename:
            print("Not saving data.")
            return
        new_file: typing.IO[str] | None = None
        try:
            print(f"Saving data to '{new_filename}'")
            new_file = open(new_filename, "w")
            new_file.write(new_content)
            print(f"Data saved in file '{new_filename}'")
        except OSError as e:
            print(f"Error opening file '{new_filename}': {e}")
        finally:
            if new_file is not None:
                new_file.close()


if __name__ == "__main__":
    main()
