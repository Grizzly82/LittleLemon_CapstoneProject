# LittleLemon_CapstoneProject
 Final Project for the Coursera Backend for Meta

/api/bookings/
/api/registration/

# littlelemon-restaurant-website

Restaurant website implemented in  ![Django](https://img.shields.io/badge/Django-092e20?style=flat&logo=django&logoColor=white)
## MAIN API ENPOINTS
```bash
/auth/token/login
/restaurant/api-token-auth
/restaurant/booking
/restaurant/menu
```
## RUN APP

### 1. Install `pipenv`

```bash
pip install pipenv
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Make database migrations

```bash
python manage.py makemigrations
```

then

```bash
python manage.py migrate
```

### 4. RUN

```bash
python manage.py runserver
```