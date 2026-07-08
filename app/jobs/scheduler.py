from apscheduler.schedulers.background import BackgroundScheduler

from app.services.ingestion_service import IngestionService


scheduler = BackgroundScheduler()


scheduler.add_job(
    IngestionService.fetch,
    trigger="interval",
    minutes=15,
    id="fetch_disaster_data",
    replace_existing=True
)


def start_scheduler():

    if not scheduler.running:
        scheduler.start()
        print("Scheduler Started...")