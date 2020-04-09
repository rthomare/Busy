echo 'See the disc-backend server run http://127.0.0.1:8000/'
echo 'hold cmd and double click on the url above'
echo 'If you want to edit react code: In a new terminal window run "./node_modules/.bin/webpack --config webpack.config.js --watch"'
source venvs/prod/bin/activate && python manage.py runserver
