==============
Add id to divs
==============

- Claim that we want to show the @display value instead of
  the title

- We want to see only the last one

- Change list_todos to use t.display instead of t.title

- In models.py, change display_fmt to ``'{title} (ID: {todo_id})'`` and
  ``def display`` to ``todo_id=self.id, title=self.title``

- Put a breakpoint on the ``def display``

    - Resume until I get to 5

- Set a watch to show the key and the value

    - ``self.display_fmt.format(todo_id=self.id, title=self.title)``

- That's inefficient, breakpoint condition

- Restart and reload browser

- Stops at the fifth item, with the watch showing the calculated value
