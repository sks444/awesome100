from requests_html import HTMLSession

from singers.models import Singer

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls000050684/')
singers = r.html.find('.lister-item')


def import_data(i, singer):
    try:
        rank = i
        url = singer.absolute_links.pop()
        name = singer.find('a')[1].text
        best_song = singer.find('a')[2].text
        summary = singer.find('p')[1].text
        image_url = singer.find('img')[0].attrs.get('src')
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Singer.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            best_song=best_song,
            summary=summary,
            image_url=image_url,
        )
        if created:
            c.save()
            print('\nSinger, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this singer: {}\n{}'
              .format(name, str(ex)))
