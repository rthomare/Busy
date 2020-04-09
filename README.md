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


