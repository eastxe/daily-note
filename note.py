#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import datetime

import click


@click.command()
@click.option('--atom', '-a', is_flag='True')
@click.option('--name', '-n')
def daily_note(atom, name):
    date = int(today())
    editor = 'atom' if atom else 'vim'
    if not os.path.exists(os.path.expanduser('~/Documents/daily-note')):
        os.mkdir(os.path.expanduser('~/Documents/daily-note'))
    if name is None:
        os.system('zsh -c "%s ~/Documents/daily-note/%d.md"' % (editor, date))
    else:
        os.system('zsh -c "%s ~/Documents/daily-note/repository/%s.md"'
                % (editor, name))


def today():
    date = datetime.datetime.today()
    return date.strftime('%Y%m%d')

if __name__ == '__main__':
    daily_note()
