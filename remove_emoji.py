#!/usr/bin/env python

import re
import sys
from typing import Pattern
from enum import IntEnum
from typing import TypeAlias


class ReturnCode(IntEnum):
    """POSIX-style return code values.

    To be used in check callable implementations.
    """

    OK = 0
    ERROR = 1

ReturnCodeType: TypeAlias = ReturnCode | int


EMOJI_PATTERN: Pattern[str] = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "]+",
    flags=re.UNICODE,
)

def remove_emojis_from_file(file_path: str) -> ReturnCode:
    """
    Remove emojis from the specified file.

    Args:
        file_path (str): The path to the file from which emojis should be removed.

    Returns:
        ReturnCode: The exit code of the hook.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content: str = file.read()

    new_content: str = EMOJI_PATTERN.sub(r"", content)

    if new_content != content:
        print(f"Removed emojis from {file_path}")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
            return ReturnCode.ERROR

    return ReturnCode.OK

def main() -> ReturnCodeType:
    """
    Main function to remove emojis from files specified in command line arguments.

    Returns:
        int: The exit code of the hook.
    """
    result: ReturnCodeType = ReturnCode.OK
    for file_path in sys.argv[1:]:
        file_result = remove_emojis_from_file(file_path)
        if file_result != ReturnCode.OK:
            result = file_result


    return result

if __name__ == "__main__":
    main()
