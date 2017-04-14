#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import datetime


def daily_note():
    date = int(today())
    os.system('zsh -c "vim ~/Documents/daily-memo/%d.md"' % date)


def today():
    date = datetime.datetime.today()
    return date.strftime('%Y%m%d')
