===============
Sorted Listings
===============

Our listings appear in the order they were added, not in alphabetical
order. Let's fix that, while making a bigger database of random
todos. We'll use this to show more debugging featuers:

- Break on exceptions

- Step Over

- Step Into

- Step Into My Code


Steps
=====

#. First, make sure you have no breakpoints open and your
   application isn't currently stopped at a breakpoint.

#. Let's change ``populate_todos`` to dynamically make some
   synthetic data, at first with a *typo* that we will later
   correct:

   .. code-block:: python

    def populate_todos():
        random_verbs = ['Make', 'Buy', 'Organize', 'Finish']
        random_nouns = ['Red', 'Apple', 'Blue', 'Tomato', 'Green', 'Pear',
                        'Black', 'Bean', 'Yellow', 'Banana', 'Brown', 'Raisin']
        for i in range(5):
            v = choice(random_verbs)
            w1 = choice(random_nouns)
            w2 = choice(random_nounsxxx)
            title = '{v} {w1} {w2}'.format(v=v, w1=w1, w2=w2)
            Todo.add(title)

#. When you save, Flask restarts, runs ``populate_todos``, and has a
   ``NameError`` on startup. You can see the traceback in the ``Debugger``
   console tab.

#. Let's change the debugger to stop on exceptions by clicking
   ``Run -> View Breakpoints``.

#. In the popup, select ``Python Exception Breakpoint -> Any Breakpoint``
   and click the checkbox for ``On raise``.

#. Re-run debugger by clicking the green ``Re-run`` button |rerun| in the
   ``5. Debug`` tool window's toolbar.


#. This time the debugger stops, but in library code. Let's fix that.

#. Go back to ``Run -> View Breakpoints``, then
   ``Python Exception Breakpoint -> Any Breakpoint`` and click the
   checkbox for ``Ignore Library Files``.

#. Re-run debugger by clicking |rerun| and execution stops on the exception
   but in our code.

#. Fix the typo by removing ``xxx`` and click the resume button
   |resume|.

#. Let's step through execution. Set a breakpoint on
   ``v = choice(random_verbs)`` by clicking in the left margin beside
   that line to create a red circle.

#. Click the ``Re-run`` button |rerun| to restart. Execution will
   stop on that line, the *first* time through the ``for`` loop.

#. Click the ``Step Over`` button |stepover| then click it again.

#. Clear your breakpoint by clicking on the red circle, then click
   ``Resume`` |resume|.

#. Let's use *Step Into* to go ``populate_todos``. Set a breakpoint
   on the line for near the end for ``populate_todos()``.

#. Re-run our debug session by clicking ``Re-run`` |rerun|. Execution
   stops on that line.

#. Click ``Step Into`` |stepinto| to go into ``populate_todos``. PyCharm
   moves the highlighted line to the first line inside that function.

#. Click ``Step Into`` |stepinto| six more times. When you reach
   ``v = choice(random_verbs)``, the debugger "steps into" the
   ``choice`` function of Python's ``random`` modules. Sometimes
   that sucks, so let's do something different.

#. Click ``Step Out`` |stepout| to get out of descending into ``choice``.
   We're back to the surface, in ``v = choice(random_verbs)``.

#. This time, click ``Step Into My Code`` |mycode| and click a couple
   more times. Note that we jump over ``choice``, because it isnt part
   of this project's code.

#. Remove the breakpoint and click ``Resume`` |resume|.

#. Now that we have a synthetic list, let's sort it. Change our
   ``Todo`` class's method ``def list`` to
   ``return sorted(todos, key=lambda todo: todo.title)``.

#. Make sure our debug session is still running, then reload your
   browser on the todo listing page. Note that the todos are sorted.

#. Re-run your debug session by clicking |rerun| and reload your
   browser. Different todo titles, but sorted.

.. |rerun| image:: https://www.jetbrains.com/help/img/idea/rerunConsole.png

.. |resume| image:: https://www.jetbrains.com/help/img/idea/debug_resume.png

.. |stepover| image:: https://www.jetbrains.com/help/img/idea/frames_step_over.png

.. |stepinto| image:: https://www.jetbrains.com/help/img/idea/frames_step_into.png

.. |stepout| image:: https://www.jetbrains.com/help/img/idea/frames_step_out.png

.. |runtocursor| image:: https://www.jetbrains.com/help/img/idea/frames_run_to_cursor.png

.. |mycode| image:: https://www.jetbrains.com/help/img/idea/step_into_my_code.png