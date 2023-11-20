from TaskManagementAPI.env_loader import PORT, HOST, DEBUG
from TaskManagementAPI import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(port=PORT, host=HOST, debug=DEBUG)