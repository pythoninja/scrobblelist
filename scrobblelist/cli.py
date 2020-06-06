#!/usr/bin/env python

import click
from tinytag import TinyTag

from scrobblelist.utils import get_mp3_files, generate_filename


@click.command()
@click.option('-d', '--directory', type=click.Path(), multiple=True, required=True,
              help='Directory where mp3 files are stored. Non-recursive')
@click.option('-r', '--recursive', type=click.BOOL, required=False, is_flag=True, help='Enables recursive search')
def cli(directory, recursive):

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


if __name__ == '__main__':
    cli()
