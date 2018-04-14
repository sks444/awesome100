import logging

from requests_html import HTMLSession

from actors.models import Actor

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls000034841/')
actor = r.html.find('.lister-item')


def import_data(i, actor):
    logger = logging.getLogger(__name__)
    try:
        rank = i
        url = actor.absolute_links.pop()
        name = actor.find('a')[1].text
        best_movie = actor.find('a')[2].text
        summary = actor.find('p')[1].text
        image_url = actor.find('img')[0].attrs.get('src')
    except Exception as ex:
        logger.error(ex)
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
            logger.info('Actor, %s has been saved.' % c)
    except Exception as ex:
        logger.error(
            'Something went wrong saving this actor: %s'
            % (ex))
