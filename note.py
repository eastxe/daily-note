#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import datetime

import click


@click.command()
@click.option('--atom', is_flag='True')
def daily_note(atom):
    date = int(today())
    editor = 'atom' if atom else 'vim'
    if not os.path.exists(os.path.expanduser('~/Documents/daily-note')):
        os.mkdir(os.path.expanduser('~/Documents/daily-note'))
    os.system('zsh -c "%s ~/Documents/daily-note/%d.md"' % (editor, date))


def today():
    date = datetime.datetime.today()
    return date.strftime('%Y%m%d')
