========
Add Todo
========

- models.py

- Replace self.id with max

- Add a static method ``def add`` that takes title

- Refactor populate_todos to use this

- Re-run models.py to confirm

- Code -> Optimize Imports to get rid of the unneeded import

- Run the app normally with the debugger

    - Stop the run config

    - Install speedups

- app.py, add a route

  .. code-block:: python

    @app.route('/todo/add', methods=['POST'])
    def add_todo():
        todo_id = request.form['todo_id']
        if todo_id:
            Todo.add(todo_id)
        return redirect('/todo/')

- Have PyCharm generate the imports

- Modify list_todos to add an input element

  .. code-block:: python

    @app.route('/todo/')
    def list_todos():
        todos = Todo.list()
        div = '<div><a href="/todo/{id}">{title}</a></div>'
        form = '''<form method="POST" action="add">
            <input name="todo_id" placeholder="Add todo..."/>
            </form>
        '''
        items = [div.format(id=t.id, title=t.title) for t in todos]
        items.append(form)
        return '\n'.join(items)

- Add a breakpoint and see the values in the scope

    - In app.py, on Todo.add line

- Reload the browser

- Show it stopping at that line, browser request is still pending

- Continue

- Browser request finishes

- Move the breakpoint to the next line, repeat

    - Doesn't require a process restart

- Clear the breakpoint


