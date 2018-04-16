from django.core.management.base import BaseCommand

from movies.get_movies import movies, import_data


class Command(BaseCommand):
    help = 'Import Movies data'

    MOVIES = staticmethod(movies)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for movie in self.MOVIES:
            self.IMPORT_DATA(i, movie)
            i = i + 1
