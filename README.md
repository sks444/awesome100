# awesome100

A curated awesome 100 list in any field.

## The Goal

This project is about collecting the best 100 profiles in any field or area. 
The Goal is to make an API with the collected data, and then we can also show a cool frontend page by making use of the API, which can be helpful for us in many ways. E.g: Every time we choose a area of work, first we search for the best profile or the best thing happend in that area till date. One can also make use of the API for their personal stuffs or websites.

## Setup Locally

* Fork and Clone the Repo
```
* $ cd awesome100
* $ pip install -r requirements.txt
```
* Create a `.env` file at the root directory of the project and put the values of the following variables in it:

```
SECRET_KEY=l3m2q5a%o(8$rq+i^gy+l_i8z6j@u1ul(i@+wanf@k6n+#=l08
DEBUG=True
DB_NAME=****
DB_USER=****
DB_PASSWORD=****
DB_HOST=127.0.0.1
ALLOWED_HOSTS=.localhost, .herokuapp.com
```

* But wait, to fill out the values of the above variables you need to have postgresql installed
on your machine and have created a new user and database. You can take help from [this guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) for the same.

* Great, we have our database. Now, it's time to fill out some data to it:

```
* $ python manage.py migrate
```

* Now, to browse to any API we need to run the management command to import those data:

E.g.: If you need all the actors data, run the following command:

```
* $ python manage.py import_best_authors
```
* Now do: `$ python manage.py runserver` and view all the actors at `http://localhost:8000/api/actors/`.

## Author

* **Shrikrishna Singh** - *Initial work* - [sks444](https://github.com/sks444)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/sks444/awesome100/blob/master/LICENSE) file for details
