from requests_html import HTMLSession

from directors.models import Director

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls056848274/')
directors = r.html.find('.lister-item')


def import_data(i, director):
    try:
        rank = i
        url = director.absolute_links.pop()
        name = director.find('a')[1].text
        best_movie = director.find('a')[2].text
        summary = director.find('p')[1].text
        image_url = director.find('img')[0].attrs.get('src')
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Director.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            best_movie=best_movie,
            summary=summary,
            image_url=image_url,
        )
        if created:
            c.save()
            print('\nDirector, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this director: {}\n{}'
              .format(name, str(ex)))
