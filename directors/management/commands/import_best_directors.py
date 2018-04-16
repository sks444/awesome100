from django.core.management.base import BaseCommand

from directors.get_directors import directors, import_data


class Command(BaseCommand):
    help = 'Import Directors data'

    DIRECTORS = staticmethod(directors)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for director in self.DIRECTORS:
            self.IMPORT_DATA(i, director)
            i = i + 1
