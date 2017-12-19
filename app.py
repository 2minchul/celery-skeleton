#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from celery import Celery
import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

# set periodic task
app.conf.beat_schedule = {
    'method_trigger': {
        'task': 'app.add',
        'schedule': 5,
        'args': (1, 2)
    },
}


@app.task
def add(x, y):
    return x + y
