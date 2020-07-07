#!/usr/bin/env python

import click
from tinytag import TinyTag

from scrobblelist.lastfm import authorize
from scrobblelist.utils import get_mp3_files, generate_filename, generate_scrobbles


@click.command()
@click.option('-d', '--directory', type=click.Path(), multiple=True, required=False,
              help='Directory where mp3 files are stored. Non-recursive.')
@click.option('-r', '--recursive', type=click.BOOL, required=False, is_flag=True, help='Enable recursive search for '
                                                                                       'mp3 files.')
@click.option('--auth', is_flag=True, help='Authorize on Last.fm.')
@click.option('--scrobble-from', type=click.Path(), help='Scrobble to Last.fm.')
def cli(directory, recursive, auth, scrobble_from):
    if auth:
        authorize()
        exit()

    if directory:
        mp3_files = get_mp3_files(directory, recursive)

        if mp3_files:
            with open(generate_filename(), 'a+') as f:
                for file in sorted(mp3_files):
                    tag = TinyTag.get(file)
                    track = f'{tag.artist} | {tag.title} | {tag.album}'
                    click.echo(track)
                    f.write(f'{track}\n')
        else:
            click.echo('No mp3 files found in provided directory')

    if scrobble_from:
        lastfm = authorize()
        scrobbles = generate_scrobbles(scrobble_from)

        if scrobbles:
            for metainfo, track_time in scrobbles.items():
                artist = metainfo.split(' | ')[0]
                title = metainfo.split(' | ')[1]
                album = metainfo.split(' | ')[2]

                lastfm.scrobble(artist=artist,
                                title=title,
                                album=album,
                                timestamp=track_time)


if __name__ == '__main__':
    cli()
