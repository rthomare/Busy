curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
pip install virtualenv
npm install --save-dev jquery react react-dom webpack webpack-bundle-tracker babel-loader babel-core babel-preset-es2015 babel-preset-react
virtualenv venvs/prod
source venvs/prod/bin/activate && pip install -r requirements.txt
source venvs/prod/bin/activate && python manage.py migrate
./node_modules/.bin/webpack --config webpack.config.js