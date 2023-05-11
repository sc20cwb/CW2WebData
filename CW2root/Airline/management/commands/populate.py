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
                for i, row in enumerate(reader):
                    # Do only 100 airports, every 700th airport
                    if i % 700 != 0:
                        continue            
                    
                    Airport.objects.create(
                        ident=row['ident'],
                        name=row['name'],
                        city=row['city'],
                        country=row['country'],
                    )

