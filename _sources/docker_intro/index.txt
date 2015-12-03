=======================
Using Docker in PyCharm
=======================

Modern development workflows emphasize isolation and reproducability
in development and production. `Docker <https://www.docker.com>`_ and
its platform approach to containers has become very popular. With
PyCharm Professional Edition 5,
`Docker is now supported <http://blog.jetbrains.com/pycharm/2015/10/announcing-pycharm-5-eap-143-165-docker-integration/>`_
as a remote interpreter.

Let's take a look at PyCharm's Docker integration in action.

Summary
=======

- Get a Django-oriented Docker image pulled locally

- Make a sample Django project

- Create a Docker interpeter to run it

- The Django run configuration makes a new container on start and
  removes it on stop

Overview
========

In Python, when you run an application -- a Django site, a database
script, etc. -- you are running it in an environment. Python has some
tools to manage the environment and make it reproducible, such as
virtual environments, pip ``requirements.txt`` files, and ``setup.py``
dependencies. But what about the non-Python parts of application?

Containers are a solution to this. In Docker, a container is an
isolated universe with software, running inside your computer. They are
fast and easy to create, start, stop, and destroy. This is ideal, not
just for development, but for deployment as well.

PyCharm 5 provides the beginning of a series of steps towards "develop
with pleasure" using containers and Docker. Namely, PyCharm 5 supports
project interpreters that are executed in a Docker container.

Preparation
===========

First, make sure ``docker`` and ``docker-machine`` are setup in your
environment. The Docker installation is painless and the website docs
are quite friendly. On non-Linux systems, you'll need a Docker "host"
virtual machine setup and running.

Next, we have to decide what software we want in our containers. In
Docker, containers are build using "images": collections of
pre-installed software and configuration that is called during
container creation. Unlike other interpreters in PyCharm, you don't
visit the ``Project Interpreter`` preferences to add Python packages.
All dependencies need to be baked into the Docker image you choose.

PyCharms doesn't manage Docker images, which makes sense, as Docker has
plenty of tools for that. This blog post expects you to use the
``minimum/docker-django-mysite`` docker image. You can fetch that onto
your system with this command:

.. code-block:: bash

    $ docker pull minimum/docker-django-mysite

Once that image is locally available, PyCharm can make Docker
interpreters for your project, as containers based on that image.

.. note::

    You have the option of making your own image as well, using a
    ``Dockerfile``. Once you make the image, you can tell PyCharm to
    make Docker interpreters based on it.

Create Django Project
=====================

Let's make a Django project, then make a Docker interpreter for it. In
PyCharm, choose ``File -> New Project``, click on ``Django``, and
follow the normal process for making a Django project.

During project creation, you'll have to use a local interpreter. If you
try to make a Docker interpreter, PyCharm will give a warning saying
you can only use a local interpreter.

The result of this step is a directory on your local computer with
sample Django code and a Django-specific PyCharm Run Configuration.

Make Docker Interpreter
=======================

On to the important part. We need to define a "remote interpreter" that
uses Docker.

Go to ``Preferences -> Project Interpreter`` and click on the gear to
the right of ``Project Interpreter`` near the top. In the
``Configure Remote Python Interpreter`` dialog, click the ``Docker``
button. You should see the following:

TODO screenshot

Click the menu dropdown for ``Machine Name``. It will likely have one
entry named ``default``. Choose that, and you will see the following:

TODO screenshot

Chosing ``default`` gave PyCharm a way to find the Docker daemon, which
can let PyCharm know which images are available locally. Hence the
dropdown for ``Images``. Click on the dropdown and choose
``minimum/docker-django-mysite:latest`` as the image, then click `Ok`.

You now have a Docker container that will be used as your project
interpreter. PyCharm features like autocomplete will be driven by this
interpreter.

Run Django
==========

Now that we have a Docker container for our project interpreter, let's
use our Django-flavored Run Configuration to run it. Just to be safe,
edit the run configuration to make sure it is using the Docker-oriented
interpreter.

What does PyCharm do when it runs this configuration:

#. First, it creates and starts a new container based on the image we
   named when creating the project interpreter.

#. This container mounts your project directory into the container at
   ``/opt/project`` in the container. *Note: On Linux, you currently
   have to perform this volume mapping manually.*

#. TODO Figure out the port mapping

#. It then executes the run configuration's Python command.

Yay, we are running a container! You can confirm this using the
following Docker commands:

.. code-block:: bash

    $ docker ps -l

This shows the most recently-run container. As you can see, our
``minimum/docker-django-mysite``-based container is currently running.

- Makes a container on each run

    - docker ps -l

- Forwards ports

    - docker ps -l

- Mounts project directory to /opt/project

    - docker exec -it big_blackwell /bin/bash

- When you stop the run window, it stops and removes the container it
  made


manage.py
=========

This integration does not yet work

Current Limitations
===================

- On Linux, you have to mount your project directory manually via
  VirtualBox

- Doesn't do docker-compose

Questions/Problems
==================

- Can I do a Flask run configuration in a Docker container?

- For Flask, import flask was broken

- Does the Pyramid run configuration work?

-

Notes
=====

- Sometimes need to do eval::

    "$(docker-machine env default)"

- https://youtrack.jetbrains.com/issue/PY-17573 is a ticket for
  discussion about Docker Compose
