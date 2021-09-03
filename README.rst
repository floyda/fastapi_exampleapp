======
To-Do App
======

Description: The classic To-Do application where a user can write down all the things he wants to accomplish.

User Stories
User can see an input field where he can type in a to-do item
By pressing enter (or a button), the User can submit the to-do item and can see that being added to a list of to-do’s
User can mark a to-do as completed
User can remove a to-do item by pressing on a button (or on the to-do item itself)
Bonus features
User can edit a to-do
User can see a list with all the completed to-do’s
User can see a list with all the active to-do’s
User can see the date when he created the to-do
When closing the browser window the to-do’s will be stored and when the User returns, the data will be retrieved


Notes
===========
* Todo item can have content, completed flag, date created
* POST new Todo to Todos
* GET all Todos
* PUT modified Todo by ID
* GET Todo by ID
* DELETE Todo by ID


Development Environment
=======================

The environment is defined through a Dockerfile and use of devcontainers in VSCode. 
To open up the environment simply open the VSCode workspace and ask to re-open in the container.

Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.

Versioning
====
This is done with https://pypi.python.org/pypi/setuptools_scm/
During the build process or maybe a pre-commit hook this should be tagged so get clean version