#!/usr/bin/env python

import time
from datetime import datetime, timedelta
from itertools import chain
from pathlib import Path
from typing import List, Tuple, Dict

FIRST_DIRECTORY = 0
TIME_DELTA: int = 5


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


def add_track_time(tracks: List[str]) -> Dict[str, int]:
    temp_time = datetime.now() - timedelta(minutes=TIME_DELTA * len(tracks))
    tracks_time = list()

    for i in tracks:
        temp_time = temp_time + timedelta(minutes=TIME_DELTA)
        track_time = int(time.mktime(temp_time.timetuple()))
        tracks_time.append(track_time)

    return dict(zip(tracks, tracks_time))


def generate_scrobbles(filepath):
    with open(filepath, 'r') as lines:
        return add_track_time(lines.read().splitlines())
