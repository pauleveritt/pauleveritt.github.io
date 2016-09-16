=========
Debugging
=========

PyCharm's graphical debugger is a key productivity feature. In some
respects,

Tasks
=====

.. toctree::
    :maxdepth: 1

    master/index.rst
    listtodos_templates/index.rst
    sorted_todos/index.rst

Notes
=====

- Add Todo

    - Run the code normally with the debugger

        - Install speedups

    - Add a breakpoint and see the values in the scope

    - Continue

    - Clear the breakpoint

- Sorted listings

    - Add more data, but with a problem in it

    - Break on exception: everything to this point is dummy, put
      in real implementation, but have an error

    - Use a loop to randomly generate titles

    - Step over (in the loop)

    - Step into (from the view, but goes into random)

    - Step Into My Code


- Delete Todo

    - Run to Cursor

    - Use Evaluate/console when stopped

    - Move back in scope/frames (to see which one is being clicked on)


- Convert to <ul>

    - Claim that we want to see the <li id=""> that's being generated

    - We want to see only the last one

    - Put a breakpoint on the list comprehension

        - Step over

    - Set a watch to show the key and the value

    - That's inefficient, breakpoint condition
