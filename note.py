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
    os.system('zsh -c "%s ~/Documents/daily-memo/%d.md"' % (editor, date))


def today():
    date = datetime.datetime.today()
    return date.strftime('%Y%m%d')
