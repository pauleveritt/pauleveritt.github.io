===========
Delete Todo
===========

- Let's start in reverse, with the UI

- app.py

- Change list_todos to add an X button

- Add a delete_todo route

- Put in a breakpoint

- Click X, confirm we have todo_id as an integer

- Click Resume

- models.py

- Add def delete

- Back in app.py, add ``todo.delete()``

- Reload browser and click X

- Stops at breakpoint

- Put cursor in model.py def delete

- Run to Cursor, make sure it's the correct todo

- Use Evaluate when stopped, self.id == 2

- In Debugger Console, click to show the Python Prompt,
  self.id == 2

- Click on Debugger tab

- Move back in scope/frames by clicking on delete_todo, to see
  what was ``todo_int`` in the previous frame

- Show new app.py and models.py

