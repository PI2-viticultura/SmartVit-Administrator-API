from flask import Flask
from flask_cors import CORS
from views.contrato import app as contrato

app = Flask(__name__)
app.register_blueprint(contrato)
CORS(app, automatic_options=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
