from celery import shared_task

@shared_task
def sample_task():
    print("🎉 Celery task executed successfully!")
    return "Task complete"
