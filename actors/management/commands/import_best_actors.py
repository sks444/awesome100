from django.core.management.base import BaseCommand

from actors.get_actors import actor, import_data


class Command(BaseCommand):
    help = 'Import AffiliatorCommitters data'

    ACTORS = staticmethod(actor)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for actor1 in self.ACTORS:
            self.IMPORT_DATA(i, actor1)
            i = i + 1
