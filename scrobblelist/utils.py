#!/usr/bin/env python

from pathlib import Path
from typing import List


def get_files(files_path: str, recursive=False):

    if recursive:
        glob_mp3_pattern: str = '**/*.mp3'
    else:
        glob_mp3_pattern: str = '*.mp3'

    mp3_files: List[Path] = list(Path(files_path).glob(f'{glob_mp3_pattern}'))

    return mp3_files
