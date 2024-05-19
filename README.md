# RateMyLandlord
## How to setup?
### How to generate the database?
```
1. python3 manage.py makemigrations

(If the code fails to generate migrations folder then try...)
python3 manage.py makemigrations landlords
python3 manage.py makemigrations reviews


2. python3 manage.py migrate
```

## How to create administrator user
```
(Create admin user for admin access in /admin url)
python3 manage.py createsuperuser
```

## How to deploy?
```
python3 manage.py runserver 0.0.0.0:<port number to host>
```

