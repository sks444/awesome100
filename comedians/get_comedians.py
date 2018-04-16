from requests_html import HTMLSession

from comedians.models import Comedian

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls052672615/')
comedians = r.html.find('.lister-item')


def import_data(i, comedian):
    try:
        rank = i
        url = comedian.absolute_links.pop()
        name = comedian.find('a')[1].text
        best_comedy = comedian.find('a')[2].text
        summary = comedian.find('p')[1].text
        image_url = comedian.find('img')[0].attrs.get('src')
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Comedian.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            best_comedy=best_comedy,
            summary=summary,
            image_url=image_url,
        )
        if created:
            c.save()
            print('\nComedian, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this comedian: {}\n{}'
              .format(name, str(ex)))
