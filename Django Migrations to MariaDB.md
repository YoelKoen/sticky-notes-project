Django Migrations to MariaDB
Transitioning from a local SQLite database to a server-based relational database like MariaDB involves a specific technical workflow:

Driver Installation: You must first install a database connector, such as mysqlclient, to allow Python to communicate with the MariaDB server.

Configuration: The DATABASES dictionary in settings.py must be updated to use the MariaDB engine and include the specific server credentials (DB Name, User, Password, Host, and Port).

Packaging Changes: Running python manage.py makemigrations scans your models.py and creates migration files that act as blueprints for the new database.

Execution: Finally, python manage.py migrate executes these blueprints on the MariaDB server, physically creating the tables and columns required for the application.