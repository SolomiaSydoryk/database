import os

from waitress import serve
import yaml

from my_project import create_app

DEVELOPMENT_PORT = 5000
PRODUCTION_PORT = 8080
HOST = "0.0.0.0"
DEVELOPMENT = "development"
PRODUCTION = "production"
FLASK_ENV = "FLASK_ENV"
ADDITIONAL_CONFIG = "ADDITIONAL_CONFIG"

if __name__ == '__main__':
    flask_env = os.environ.get(FLASK_ENV, DEVELOPMENT).lower()
    config_yaml_path = os.path.join(os.getcwd(), 'config', 'app.yml')

    with open(config_yaml_path, "r", encoding='utf-8') as yaml_file:
        config_data_dict = yaml.load(yaml_file, Loader=yaml.FullLoader)

        if flask_env == DEVELOPMENT:
            config_data = config_data_dict[DEVELOPMENT]
            create_app(config_data).run(port=DEVELOPMENT_PORT, debug=True)

        elif flask_env == PRODUCTION:
            config_data = config_data_dict[PRODUCTION]
            serve(create_app(config_data), host=HOST, port=PRODUCTION_PORT)

        else:
            raise ValueError(f"Check OS environment variable '{FLASK_ENV}'")
