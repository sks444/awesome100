from requests_html import HTMLSession

from authors.models import Author

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls005774742/')
authors = r.html.find('.lister-item')


def import_data(i, author):
    try:
        rank = i
        url = author.absolute_links.pop()
        name = author.find('a')[1].text
        best_book = author.find('a')[2].text
        try:
            summary = author.find('p')[1].text
        except Exception as ex:
            summary = ''
        image_url = author.find('img')[0].attrs.get('src')
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Author.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            best_book=best_book,
            summary=summary,
            image_url=image_url,
        )
        if created:
            c.save()
            print('\nAuthor, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this author: {}\n{}'
              .format(name, str(ex)))
