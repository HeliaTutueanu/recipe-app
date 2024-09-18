# Recipe App
## Project description
A recipe app with a PostgreSQL database at the server side, and the client side renders HTML- and CSS-based pages via the Django framework. This application lets the users sign up and create their own content. The user can create and edit recipes, including their ingredients, cooking time, and difficulty level.

## Project Exploration
On the homepage, the user can click on ```Create new recipe``` to add a new recipe.

When viewing the details of a recipe, users have the option to click on ```Update``` to modify the recipe. However, this functionality is restricted to the user's own recipes and cannot be applied to recipes of other users.

When viewing the details of a recipe, users have the option to click on ```Delete``` to remove the recipe. However, this functionality is restricted to the user's own recipes and cannot be applied to recipes of other users.

When searching for recipes or ingredients, users have the option to view data analytics of the search results in formats such as 'Bar Chart,' 'Line Chart,' or 'Pie Chart,' displayed below the search results.


## Project dependencies
### Dependencies used in development
* Django (4.2.11)
* pillow (10.2.0)
* pandas (2.0.3)
* matplotlib (3.7.5)
* django-environ (0.11.2)
* numpy (1.24.4)

### Dependencies used in production
* gunicorn (21.2.0)
* dj-database-url (2.1.0)
* psycopg2-binary (2.8.6)
* whitenoise (6.6.0)
* Brotli (1.1.0)

## Key Features
* Allow for user authentication, login, and logout.
* Let users search for recipes according to ingredients.
* Automatically rate each recipe by difficulty level.
* Receive user input and handle errors appropriately.
* Display more details on each recipe if the user asks for that.
* Add user recipes to an database.
* Include a Django Admin dashboard for working with database entries.
* Show statistics and visualizations based on trends and data analysis

## Technical Requirements
* Works on Python 3.6+ installations and Django version 3.
* Handles exceptions or errors that arise during user input, for example, then displays user-friendly error messages.
* Connects to a PostgreSQL database hosted locally on the same system (an SQLite database is needed during the development of your application).
* Provides an easy-to-use interface, supported by simple forms of input and concise, easy-to-follow instructions. Menus containing features like login and logout must be presented neatly—with concise and easy-to-follow prompts.

## Set up this App
1. Clone this repository.
2. Navigate to the recipe-app folder and run ```make install-dev```
3. Setup Database by configuring ```DATABASES``` in the ```settings``` folder in ```dev.py``` for development.
4. Run migrations with ```make dev-migrate```
5. Create a superuser by running ```make dev-superuser```
6. Run ```make dev-start``` to check out the app in your browser under ```http://127.0.0.1:8000```