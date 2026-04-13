#!/usr/bin/env python3


def secure_archive(
    filename: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    """Provide safe access to a file for reading and writing"""
    if mode not in ("r", "w"):
        return (False, "Invalid mode, use 'r' or 'w'")
    try:
        if mode == "r":
            with open(filename, "r") as file:
                content = file.read()
            return (True, content)
        else:
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
    except OSError as e:
        return (False, str(e))


def main() -> None:
    """Run the main program."""
    print(secure_archive("/not/existing/file", "r"))
    print(secure_archive("/etc/master.passwd", "r"))
    print(secure_archive("ancient_fragment.txt", "r"))
    print(secure_archive("ancient_fragment.txt", "w", "Test_input123"))


if __name__ == "__main__":
    main()
