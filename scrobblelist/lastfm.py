#!/usr/bin/env python

import os
import time
from pathlib import Path

import pylast

API_KEY: str = os.getenv('LASTFM_API_KEY')
API_SECRET: str = os.getenv('LASTFM_API_SECRET')
SESSION_KEY_FILE: Path = Path.home() / '.scrobblelist'


def authorize() -> pylast.LastFMNetwork:
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
    lastfm_session = pylast.SessionKeyGenerator(network)

    if not SESSION_KEY_FILE.exists():
        auth_url = lastfm_session.get_web_auth_url()
        print(f'Open your browser and authorize application: {auth_url}')

        while True:
            try:
                session_key = lastfm_session.get_web_auth_session_key(auth_url)
                SESSION_KEY_FILE.write_text(session_key)
                print(f'Session key has been saved to {SESSION_KEY_FILE}')
                break
            except pylast.WSError:
                time.sleep(1)
    else:
        print(f'You are already authorized with session this key: {get_session_key()}')
        print(f'Session key file location: {SESSION_KEY_FILE}')

    network.session_key = get_session_key()

    return network


def get_session_key():
    if SESSION_KEY_FILE.exists() and SESSION_KEY_FILE.stat().st_size > 0:
        return SESSION_KEY_FILE.read_text()
    else:
        print('Something wrong with session key file, try to remove ~/.scrobblelist file and run --auth again')
        exit()
