from django.core.management.base import BaseCommand

from singers.get_authors import singers, import_data


class Command(BaseCommand):
    help = 'Import Singers data'

    SINGERS = staticmethod(singers)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for singer in self.SINGERS:
            self.IMPORT_DATA(i, singer)
            i = i + 1
