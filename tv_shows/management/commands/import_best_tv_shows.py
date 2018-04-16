from django.core.management.base import BaseCommand

from tv_shows.get_tv_shows import tv_shows, import_data


class Command(BaseCommand):
    help = 'Import TvShows data'

    TV_SHOWS = staticmethod(tv_shows)
    IMPORT_DATA = staticmethod(import_data)

    def handle(self, *args, **options):
        i = 1
        for tv_show in self.TV_SHOWS:
            self.IMPORT_DATA(i, tv_show)
            i = i + 1
