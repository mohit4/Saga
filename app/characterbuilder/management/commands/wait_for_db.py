import time

from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Command will wait for the DB to come online before proceeding further"""

    def handle(self, *args, **kwargs):
        self.stdout.write('Checking db connection...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write(self.style.WARNING('Database unavailable, waiting...'))
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS("Database available!"))