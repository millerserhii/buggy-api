## Buggy API

this is a demo project to assess the junior Django developers. It is designed for live assessment. 

The project contain 1 app Movies with 3 models  - Movie, Rating and Catalog.

The base serializers are implemented

Movie models are tested with pytest.

The participant should finish this assessment within 1 hour. 

### Start project

create and activate virtual env

```bash
python -m venv venv
source venv/bin/activate
```

install all requirements

```
pip install -r requierements.txt
```

make migrations

```
python manage.py makemigrations
```

run the app

```
python manage.py runserver
```

#### Testing

```
pytest
```


### Tasks to a participant

1. Finish model methods get_average_rating and lock_catalog
2. add token authentication with djoser (https://djoser.readthedocs.io/en/latest/getting_started.html)
3. Add views with IsAuthenticated permissions
4. *Add possibility for superuser to lock someone's catalog
5. *Add tests endpoint tests

#### Authors

created by Sergej Müller
