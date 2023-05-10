import csv
import random
from django.core.management.base import BaseCommand
from Airline.models import Airport

file_path = 'airline/airports.csv'
random.seed(42)
#

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                airports = random.sample(list(reader), 100)
                
                for row in airports:
                    # If airport already exists by ident or name, skip it
                    Airport.objects.create(
                        ident=row['ident'],
                        name=row['name'],
                        city=row['city'],
                        country = row['country']
                    )
