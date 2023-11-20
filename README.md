# Setting Up .env

To run this application, follow these steps:

1. **Create a `.env` File:**

   Create a file named `.env` in the root directory of your project.

2. **Insert the Following Credentials:**

   Open the `.env` file and insert the following lines, replacing the placeholders with your actual credentials:

   ```env
   # .env

	DEBUG=True
	PORT=5000
	HOST=0.0.0.0
	DB_URI=postgresql://postgres:root@localhost:5432/TaskManager

   	SECRET_KEY=your_flask_secret_key
   ```

   Adjust these values based on your specific database and application configuration.

3. **Save and Close the File:**

   Save the changes to the `.env` file and close it.



# Database Migrations

Below are the common commands used for managing database migrations in a Flask application using Flask-Migrate and Flask-Script.

1. **Initialize the Migration Repository:**
   ```bash
   python manage.py db init
   ```

   This command initializes a new migration repository. Run this command only once when setting up your project.

2. **Generate a Migration:**
   ```bash
   python manage.py db migrate -m "Your migration message"
   ```

   This command generates a new migration based on changes in your models. Run this command every time you make changes to your database models.

3. **Apply Migrations:**
   ```bash
   python manage.py db upgrade
   ```

   This command applies any pending migrations to the database.

4. **Downgrade a Migration:**
   ```bash
   python manage.py db downgrade
   ```

   This command rolls back the last applied migration. Use it with caution, especially in production environments.

5. **Show the List of Migrations:**
   ```bash
   python manage.py db history
   ```

   This command displays a list of migrations and their statuses.

6. **Show the Current Revision:**
   ```bash
   python manage.py db current
   ```

   This command shows the current revision of the database.

