===============
Initial ToDoMVC
===============

In this second section, we're going to rewrite a Flask-based ToDo
application, because, hey, don't we all love a good todo demo. In
this case, we'll model it after the various
`ToDoMVC <http://todomvc.com>`_ implementations. That is, our starting
point will have:

- `Flask <http://flask.pocoo.org>`_ and
  `Flask-Restless <https://flask-restless.readthedocs.org/en/stable/>`_
  with SQLite

- jQuery which fetches/updates the data and redraws the HTML using
  simple jQuery-based client-side templating implementation

Python Setup
============

Let's get started. We have a Flask application. We aren't going to
distribute it, so we don't need a ``setup.py``. But to keep ourselves
sane, let's make a ``requirements.txt`` for dependencies:

.. literalinclude:: requirements.txt
    :caption: requirements.txt Python dependencies
