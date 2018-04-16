from django.core.management.base import BaseCommand

from comedians.get_comedians import comedians, import_data


class Command(BaseCommand):
    help = 'Import Comedians data'

    COMEDIANS = staticmethod(comedians)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for comedian in self.COMEDIANS:
            self.IMPORT_DATA(i, comedian)
            i = i + 1
