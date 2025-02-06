# Report power bi app

This project was made with django!

# Installation
In the root project, run:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Go to: http://127.0.0.1:8000/

![alt text](./readmeImg/login.png)

# Create superuser
when you start a new project, there is no user login. 
Stop the local server Django service and run:
```
python manage.py createsuperuser

``` 

Insert the username and password and now you can Sing in.

![alt text](./readmeImg/usernameLogin.png)

