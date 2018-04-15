from requests_html import HTMLSession

from actors.models import Actor

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls000034841/')
actor = r.html.find('.lister-item')


def import_data(i, actor):
    try:
        rank = i
        url = actor.absolute_links.pop()
        name = actor.find('a')[1].text
        best_movie = actor.find('a')[2].text
        summary = actor.find('p')[1].text
        image_url = actor.find('img')[0].attrs.get('src')
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Actor.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            best_movie=best_movie,
            summary=summary,
            image_url=image_url,
        )
        if created:
            c.save()
            print('\nActor, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this actor: {}\n{}'
              .format(name, str(ex)))
