=========
Debugging
=========

.. note::

    This is a placeholder for expanded material to go beyond the
    2.5 hour tutorial. The code for this and the transcript notes
    are already completed.

Tasks
=====

.. toctree::
    :maxdepth: 1

    master/index.rst
    listtodos_templates/index.rst


Sorted Listings
===============

- Excuse to do simple Python debugging (no stepping)

- Back in models.py, we're going to change ``def list`` to return
  a sorted listing

- First, right-click Debug to run it under the debugger

- Then, refactor to extract the return value into a local variable

- Change to assign a sorted list to that variable

- Set a breakpoint on the assignment

- Ctrl-D and confirm

Todo Comment Counts
===================

- Excuse to debug by stepping through a loop in Python

- Add a fake count of comments, in parentheses, in the listing of
  todos

- Gets a ``@property`` of comments on the class

- This calls some loop which assembles five primes, then randomly
  selects one (as a way to later use the profiler if possible)


