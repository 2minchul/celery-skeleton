## Running the Celery worker server

### work in foreground
```bash
celery -A app worker -l info
```

### work in background
```bash
celery multi start -A app worker --logfile=worker.log

# Stop background Worker
celery multi stop worker
```

### run Celery Beat
```bash
# foreground
celery -A app beat

# run worker & beat in the background
celery multi start -A app worker --beat
```