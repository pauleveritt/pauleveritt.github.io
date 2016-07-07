================
Debugging Python
================

Switch to Master Template
=========================

- Excuse to run under the debugger and install Cython extensions

- Stop the Run tool window's execution

- Make templates/layout.html, using Emmet for completion

- Make home_page.html but *not* in templates directory

- Change home_page to return render_template('index.html', title='Home Page')

- Quick Fix to import render_template

- PyCharm warns us that the template can't be found

- Right-click, Refactor, Move (can also be drag-and-drop)

- Right-click on ``app.py``, Debug

- Reload browser

- All is normal

List/Show Todos Template
========================

- Excuse to show debugger breakpoint in Jinja2

- Convert other 2 views to Jinja2

- Start with Show Todo, but pass in page_title instead of title,
  get exception in Flask

- Put breakpoint in layout.html, show the local context has
  page_title

- Fix, reload

- Change list_todos to a template with a Jinja2 for loop

- Put a breakpoint in the template, iterate over the loop

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


