from requests_html import HTMLSession

from tv_shows.models import TvShow

session = HTMLSession()
r = session.get(  # Ignore PycodestyleBear (E501)
    'http://www.imdb.com/list/ls004729995/?sort=moviemeter,asc&st_dt=&mode=detail&page=1')  # Ignore LineLengthBear
tv_shows = r.html.find('.lister-item')


def import_data(i, tv_show):
    try:
        rank = i
        name = tv_show.find('h3')[0].find('a')[0].text
        url = ('http://www.imdb.com'
               + tv_show.find('h3')[0].find('a')[0].attrs.get('href'))
        summary = tv_show.find('p')[1].text
        rating = tv_show.find('.ipl-rating-star__rating')[0].text
        image_url = tv_show.find('img')[0].attrs.get('src')
        genre = tv_show.find('.genre')[0].text
        try:
            duration = tv_show.find('.runtime')[0].text
        except:
            duration = ''
        actors_and_directors = tv_show.find('.text-muted')[2].text
        votes_and_gross = tv_show.find('.text-muted')[3].text
        try:
            other_info = tv_show.find('.list-description')[0].text
        except:
            other_info = ''
    except Exception as ex:
        print(str(ex))
    try:
        c, created = TvShow.objects.get_or_create(
            rank=rank,
            url=url,
            name=name,
            summary=summary,
            image_url=image_url,
            rating=rating,
            genre=genre,
            duration=duration,
            actors_and_directors=actors_and_directors,
            votes_and_gross=votes_and_gross,
            other_info=other_info,
        )
        if created:
            c.save()
            print('\nTvShow, {}, has been saved.'.format(c))
    except Exception as ex:
        print('\n\nSomething went wrong saving this tv_show: {}\n{}'
              .format(name, str(ex)))
