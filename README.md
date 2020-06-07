# scrobblelist

## About

Project description

## Installation

Just run `pip install scrobblelist` or clone this repo and run `command to run`

## Features

Features list

## Usage

### Select source directory

`scrobblelist -d | --directory` -- directory where mp3 files are located. It will not search for files recursively.

Output sample:

```
scrobblelist --directory '/home/user/Music/O.N.A/01. O.N.A/[1998] T.R.I.P'

O.N.A. | Nie Chcę Nigdy - Babcia | T.R.I.P.
O.N.A. | Najtrudniej | T.R.I.P.
O.N.A. | Temu, Który Jest | T.R.I.P.
O.N.A. | Czarna Myśl | T.R.I.P.
O.N.A. | Rośnie We Mnie Gniew | T.R.I.P.
O.N.A. | Nienawidzę | T.R.I.P.
O.N.A. | Kwaśna Przygoda | T.R.I.P.
O.N.A. | Hystoryjka | T.R.I.P.
O.N.A. | To Naprawde Już Koniec | T.R.I.P.
```

`scrobblelist --directory '/home/user/Music/O.N.A/01. O.N.A/ --recursive`

Output sample:

```
O.N.A. | Znalazłam | Modlishka
O.N.A. | Koła Czasu | Modlishka
O.N.A. | Cwany | Modlishka
O.N.A. | Drzwi | Modlishka
O.N.A. | Wszystko dla ciebie mam | Modlishka
...
O.N.A. | Białe Ściany | Bzzzzz
O.N.A. | Kiedy Powiem Sobie Dość | Bzzzzz
O.N.A. | Krzyczę – Jestem | Bzzzzz
O.N.A. | 24 Godziny Po... | Bzzzzz
O.N.A. | W Mojej Głowie | Bzzzzz
```

Output format is compatible for [@scrobblerbot](tg://resolve?domain=scrobblerBot) multiple scrobbling feature.

### Last.fm Authentication

`scrobblelist --auth`

This command will generate authentication link and after you allow access to application, it will save session key to
`~/.scrobblelist` file.

### Last.fm Scrobbling

There are two ways you can scrobble. You should run --auth command first to work with scrobbling: 

1. `scrobblelist scrobble --from-file filepath`
2. `scrobblelist scrobble --from-dir dirpath`

## Why?

Why I did it?

## Development

Development process
