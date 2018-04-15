from django.core.management.base import BaseCommand

from authors.get_authors import authors, import_data


class Command(BaseCommand):
    help = 'Import AffiliatorCommitters data'

    AUTHORS = staticmethod(authors)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for author in self.AUTHORS:
            self.IMPORT_DATA(i, author)
            i = i + 1
