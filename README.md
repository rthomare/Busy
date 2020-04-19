This is a django application

Getting started:
Install Django: https://docs.djangoproject.com/en/1.11/intro/install/
Install DB: https://docs.djangoproject.com/en/1.11/topics/install/#database-installation POSTGRESQL
TBD

"Soft" Dev Enviornment Setup:
- Download node.js from the following link: https://nodejs.org/en/download/

- Copy and rename /local_settings.py.template to /local_settings.py.template add the following file.

- run ```sudo ./init.sh```
	- You will be prompted to enter your computer password.

- run ```sudo ./start.sh```

- If you want to do react active development open a new terminal window and run:
	- ```./node_modules/.bin/webpack --config webpack.config.js --watch```

**If you run into problems with running the above command try running the following commands:**

- ```sudo chown `whoami` ./Configs/static/bundles/index.js```
- ```sudo chown `whoami` ./Configs/static/bundles/aboutus.js```

# Suggested Deployment

I recommend deploying to a heroku server. For information see https://devcenter.heroku.com/articles/deploying-python
1. Create a heroku application: https://heroku.com
2. From heroku add the following
    - (Free) Add a postgres hobby-dev database add-on to your server: https://devcenter.heroku.com/articles/heroku-postgresql
3. Update the environment variables to the following: https://ibb.co/jf8DFXQ
  a. Note inorder to get the giphy search api to work you'll need to get a giphy api key: https://developers.giphy.com
4. Deploy the app: ```git push heroku master```
5. Using the heroku command line add run the following commands:
    - heroku run ```python manage.py makemigrations```
    - heroku run ```python manage.py migrate```
    - heroku run ```python manage.py collectstatic```
6. Lastly you'll want to create superuser(s) to be effectly add, remove, and change data.
    Following: https://docs.djangoproject.com/en/1.8/intro/tutorial02/#creating-an-admin-user
    - heroku run ```python manage.py createsuperuser```
7. Go to your website and go to the admin section "www.xxxx-herokuapp.com/admin/", log in as the superuser you just created, add some new Person objects, and you are good to go!