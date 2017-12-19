## Running the Celery worker server

### Work in foreground
```bash
celery -A app worker -l info
```

### Work in background
```bash
celery multi start -A app worker --logfile=worker.log

# Stop background Worker
celery multi stop worker
```

### Run Celery Beat
```bash
# foreground
celery -A app beat

# run worker & beat in the background
celery multi start -A app worker --beat
```