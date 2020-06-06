#!/usr/bin/env python

from datetime import datetime
from itertools import chain
from pathlib import Path
from typing import List, Tuple

FIRST_DIRECTORY = 0


def get_mp3_files(directory: Tuple, recursive: bool) -> List[Path]:
    if len(directory) == 1:
        return scan_directory(directory[FIRST_DIRECTORY], recursive=recursive)
    else:
        files = []
        for i, d in enumerate(directory):
            files.append(scan_directory(directory[i]))

        return list(chain.from_iterable(files))


def scan_directory(files_path: str, recursive=False) -> List[Path]:
    if recursive:
        glob_mp3_pattern: str = '**/*.mp3'
    else:
        glob_mp3_pattern: str = '*.mp3'

    return list(Path(files_path).glob(f'{glob_mp3_pattern}'))


def generate_filename() -> str:
    now: datetime = datetime.now()
    return now.strftime("scrobblelist-%Y-%m-%d_%H-%M-%S.txt")
