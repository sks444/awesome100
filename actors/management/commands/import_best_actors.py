from django.core.management.base import BaseCommand

from actors.get_actors import actors, import_data


class Command(BaseCommand):
    help = 'Import Actors data'

    ACTORS = staticmethod(actors)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for actor in self.ACTORS:
            self.IMPORT_DATA(i, actor)
            i = i + 1
