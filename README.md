# Heroku Spiders

## Package manager setup

We will use pipenv which is a package manager for Python similar to javascript's npm. The good thing about pipenv is that it creates a virtual environment for the project and then install dependencies inside the project. So you can develop and run your project in this separate virtual environment with all the required dependencies.

To install pipenv you run:

```bash
sudo pip install pipenv
```

To initialize a Python 3 project with pipenv run:

```bash
pipenv install --three
```

When you run the pipenv install two files will be created the `Pipfile` and the `Pipfile.lock`

To install a Python package for your project you have to use the `install` keyword. For example to install Flask:

```bash
pipenv install Flask
```

To uninstall Flask:

```bash
pipenv uninstall Flask
```

To install a specific version of a package:

```bash
pipenv install requests==2.13.0
```

When you clone a repository to fetch all the dependencies just run:

```bash
pipenv install
```

To install dependencies that are only needed for the development process use the --dev flag, for example to install testing dependencies:

```bash
```

In order to activate the virtual environment associated with your Python project you can simply use the shell keyword:

```bash
pipenv shell
```

To leave this virtual environment you just type `exit`.

You can also invoke shell commands in your virtual environment, without explicitly activating it first, by using the run keyword. For example:

```bash
## pipenv run python <name_of_file>
pipenv run python server.py
```

## Create Flask App

For the initial deployment setup we will have a very simple Flask application and we show how to setup a more complex application later.

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

```

## Deploying Python applications on Heroku

To deploy Python applications on heroku we will use Gunicorn. The reason is that the Flask web framework has built-in web server, but these blocking server only process a single request at a time. If you deploy with this server on Heroku, your dyno resources will be underutilized and your application will feel unresponsive.
Gunicorn is a pure-Python HTTP server for WSGI applications. It allows you to run any Python application concurrently by running multiple Python processes within a single dyno.

To add Gunicorn to our project:

```bash
pipenv install gunicorn
```

Now we need to create a folder for our app and inside create a `__init__.py` file which will expose the application.

```python
# inside __init__.py
from .app import app
```

Now we can serve our application using Gunicorn:

```bash
# -b HOST:PORT <module_name>:<app>
gunicorn -b 127.0.0.1:3000 skeleton_app:app
```

Next we need to create the Procfile for Heroku, below is the simple version if you need more customization check the Gunicorn documentation:

```txt
web: gunicorn skeleton_app:app
```

To test our heroku setup locally before pushing it we can run:

```txt
heroku local web
```
