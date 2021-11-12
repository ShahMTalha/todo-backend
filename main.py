import os
from dotenv import load_dotenv

load_dotenv()

from src.app import create_app

app_settings = os.environ.get('APP_SETTINGS')
app = create_app(app_settings)
host = os.environ.get('FLASK_HOST','0.0.0.0')
port = os.environ.get('FLASK_PORT','5000')

if __name__ == '__main__':
    app.run(host=host, port=port, debug=False)
