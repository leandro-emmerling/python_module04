#!/usr/bin/env python3


import sys
import typing


def main() -> None:
    """Run the main Program."""
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file: typing.IO[str] | None = None
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        file = open(sys.argv[1], "r")
        print("---\n")
        print(file.read())
        print("---")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if file is not None:
            file.close()
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
