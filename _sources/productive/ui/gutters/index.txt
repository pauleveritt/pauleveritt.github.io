==============
Editor Gutters
==============

PyCharm's editor allows, obviously, editing. But the left and right
margin's, aka the gutters, have rich functionality for helping you
code. Let's

Steps
=====

- Add a route with one error and two warnings:

   .. code-block:: python

        @appx.route('/todo')
        def list_todos() :
            x = 1
            return 'Todos List'

- Reload browser, see the problems

- Emphasize the extra space before the colon

- Explain fixing the error

- Explain fixing the format warning

- Explain fixing the unused variable warning

- Toggle line numbers in the left gutter

- Reload browser, see the fixes

Analysis
========


Extra Credit
============

- Delete the flask import line, then have PyCharm generate the import for you


TODO
====