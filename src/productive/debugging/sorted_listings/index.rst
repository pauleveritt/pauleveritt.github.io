===============
Sorted Listings
===============

- Add more data, but with a problem in populate

- On Flask reload, it fails with NameError

- Debugger -> View Breakpoints -> Python Exception Breakpoint
  Any Breakpoint -> Check ``On Raise``

- Re-run debugger

- Stops in library code, which sucks

- Re-open that View Breakpoints, check ``Ignore Library Files``

- Re-run debugger, stops on the exception

- Fix bug

- Set breakpoint on ``v = choice(random_verbs)``

- Step over (in the loop)

- Clear breakpoint, click Resume

- Set breakpoint on ``todo = Todo(title)``

- Restart debugger

- Step into (goes into __init__)

    - Step into again

    - Eventually goes into randint

    - Step out and close ``random.py``

- Resume and step into __init__

- Now use Step Into My Code, doesn't open

- Clear the breakpoint

- Click ``Resume`` in the debugger

- Change ``def list`` to
  ``return sorted(todos, key=lambda todo: todo.title)``

- Reload in browser and compare