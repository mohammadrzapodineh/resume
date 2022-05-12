# Resume Project
This is A Resume App Who created With Django And You can Run This Application With Docker I Hope Useful For You Enjoy it


# Preview
- [Resume app](https://qrcodes.s3.ir-thr-at1.arvanstorage.com/Capture.PNG)



## Dependences

- Django
- Docker
- Gunicorn
- Nginx
- PostgreSql


# How To Run?
For Run You must Install Docker



You installed Docker In The First Step You must Create  The Volumes And Networks

- For Create Volumes
```
docker volume create db_volume
docker volume create app_static_volume
docker volume create nginx_network
```
```
docker network create nginx_network
docker network create app_network
```
In the next step you must create a .env file in the project directory for example you can open
and read the .env_example and Copy default values in for .env file

- ##### values
```
EMAIL_HOST_PASSWORD="Password Of Email Host"
EMAIL_HOST_USER="Your Email Host"
EMAIL_PORT=587
EMAIL_USE_TLS=True
RECAPTCHA_PUBLIC_KEY="Your Public Key v3"
RECAPTCHA_PRIVATE_KEY="Your Secret Key V3"
POSTGRES_DB=app_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=Your Password User for Db
SECRET_KEY = 'django-insecure-v6ay3@@+2z&zc(f_oep=*68dto7hb_=pp_3qisij_$xlbhm$v!'
```
Hint: This Project Use Recaptcha v3 Google And you must create a captcha for you and insert
your captcha information in .env file and for Replay To Users Messages Project must connect To  a SMTP service
you can use Google SMTP For More Information Please Read The below Article
- [SMTP Send With Django](https://www.section.io/engineering-education/how-to-send-email-in-django/)

Now We must Run Django And PostgreSql db  and Nginx With docker-compose

````
docker-compose up -d
````
For Run Nginx
```
cd config/nginx/
docker-compose up -d
```
Now open The  Browser And you can access The Project With http://localhost