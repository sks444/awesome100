from requests_html import HTMLSession

from movies.models import Movie

session = HTMLSession()
r = session.get('http://www.imdb.com/list/ls055592025/')
movies = r.html.find('.lister-item')


def import_data(i, movie):
    try:
        rank = i
        name = movie.find('h3')[0].find('a')[0].text
        url = ('http://www.imdb.com'
               + movie.find('h3')[0].find('a')[0].attrs.get('href'))
        summary = movie.find('p')[1].text
        rating = movie.find('span')[8].text
        image_url1 = movie.find('img')[0].attrs.get('src')
        genre = movie.find('.genre')[0].text
        duration = movie.find('.runtime')[0].text
        actors_and_directors = movie.find('.text-muted')[2].text
        votes_and_gross = movie.find('.text-muted')[3].text
        other_info = movie.find('.list-description')[0].text
    except Exception as ex:
        print(str(ex))
    try:
        c, created = Movie.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            summary=summary,
            image_url=image_url1,
            rating=rating,
            genre=genre,
            duration=duration,
            actors_and_directors=actors_and_directors,
            votes_and_gross=votes_and_gross,
            other_info=other_info,
        )
        if created:
            c.save()
            print('\nMovie, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this movie: {}\n{}'
              .format(name, str(ex)))
