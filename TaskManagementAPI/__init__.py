from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from TaskManagementAPI.configs.configs import Config
from TaskManagementAPI.configs.logger_config import logger
from TaskManagementAPI.errors.error_handler import CustomError


# create Flask application 
app = Flask("Task Management Application")

# Added all the Configs on the Application
app.config.from_object(Config)

# initialize the SQLAlchemy
db = SQLAlchemy(app)

# initialize the Marshmallow
ma = Marshmallow(app)


# initialize the Migrate 
migrate = Migrate(app, db)

# The errorhandler for the app will help to log the error in the logger and here we can 
# manupulae any error things. For Example we can send mail also. 
@app.errorhandler(CustomError)
def handle_custom_error(error):
    if error.log == True:
        # logging the error. 
        logger.error(f"{error.error_message} in {error.module_name}.{error.function_name}")
    return {'error': error.error_message}, error.status_code



# create factory function
def create_app(config_class=Config):

    # register all the blue prints
    from TaskManagementAPI.APIs.Auth.auth_view import auth_blueprint
    app.register_blueprint(auth_blueprint)

    from TaskManagementAPI.APIs.GraphQL_ import graph_ql_b
    app.register_blueprint(graph_ql_b)

    from TaskManagementAPI.APIs.Assigns.assign_view import assigns_b
    app.register_blueprint(assigns_b)

    from TaskManagementAPI.APIs.Org.org_view import org_b
    app.register_blueprint(org_b)

    from TaskManagementAPI.APIs.Schedule.schedule_view import schedule_b
    app.register_blueprint(schedule_b)

    from TaskManagementAPI.APIs.Tasks.task_view import task_b
    app.register_blueprint(task_b)

    from TaskManagementAPI.APIs.Users.user_view import user_b
    app.register_blueprint(user_b)

    return app