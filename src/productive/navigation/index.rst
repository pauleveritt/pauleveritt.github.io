==========
Navigation
==========

Add Todo Views
==============

- Excuse to show one pattern of navigation: open most recently edited

- Close all tabs

- Right-click in Project root, Find in Path, type in ``class Todo``,
  narrow by .py

- Click Preview tab, single click entry to preview, double click to open

- Add a @staticmethod for ``add``

- We now need to add the route, which is in ``app.py``

- Right-click on ``Todo`` in ``class Todo`` and choose ``Find Usages``

- Note the shortcut: Alt-F7

- That opens a tool window, let's try something else, so dismiss
  the ``Find`` tool by clicking on ``4. Find``

- What other flavors of "Find Usage" are there? Let's use "Search
  Actions", Cmd-Shift-A (very useful) "usages"

- Make sure your cursor is still on ``Todo``

- Let's try Show Usages (and note its shortcut)

- Choose the first entry for app.py

- Close ``models.py``

- Put in the route in ``app.py``

- We decide we want to go run ``models.py`` to confirm that add works

- In ``app.py``, click on Todo, Cmd-B

- Put a dummy implementation in main block

- Run it, confirm it works

- Alt-leftarrow to jump back to where you were

- Now need to add an input box on the list todos template

- Close all open tabs (just to emphasize)

- Let's jump to that file with Navigate -> File (Cmd-Shift-O), list.html

- Use Emmet to make the input

- Realize we need a form, but can't remember "Surround with Emmet"...wait,
  that needs a selection, what is "Extend Selection"?

- Cmd-Shift-A, Extend

- Need it again...Cmd-Shift-A...now have the input selected, time to
  "surround with Emmet"

- Cmd-Shift-A, SuEm, camel case surround with Emmet

- ``form`` enter to do Emmet for making a form

- Re-load browser

- Explain Help -> Keymap Reference


Delete Todo
===========

- That was a lot...let's do another route, repeating many of those
  navigation/lookup techniques, while adding a few more

- Navigate - Class

- Navigate Symbol, with camel case

- Super search
