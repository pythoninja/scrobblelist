#!/usr/bin/env python

import click
from tinytag import TinyTag

from scrobblelist.utils import get_mp3_files


@click.command()
@click.option('-d', '--directory', type=click.Path(), multiple=True, required=True,
              help='Directory where mp3 files are stored. Non-recursive')
@click.option('-r', '--recursive', type=click.BOOL, required=False, is_flag=True, help='Enables recursive search')
def cli(directory, recursive):

    mp3_files = get_mp3_files(directory, recursive)

    if mp3_files:
        for file in sorted(mp3_files):
            tag = TinyTag.get(file)
            click.echo(f'{tag.artist} | {tag.title} | {tag.album}')
    else:
        click.echo('No mp3 files found in provided directory')


if __name__ == '__main__':
    cli()
