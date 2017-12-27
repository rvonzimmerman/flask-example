# Simple Flask Application
## To get up and running, do the following:

* Install the requirements with:
```
pip install -r requirements.txt
```
* Edit the `dev.cfg` file to point to a working mysql database.
Alternatively, plug in your favorite db connector.

* Apply the database migrations:

    ``
    flask db upgrade
    ``


* Run the application with:

    ``
    FLASK_APP=web-start.py flask run
    ``

* Currently, the available routes are `/blog` and `/accounts`. Check out the associated
blueprints for how they work.

