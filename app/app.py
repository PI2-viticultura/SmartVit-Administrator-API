from flask import Flask
from flask_cors import CORS
from views.contract import app as contract
from views.order import app as order
from views.partner import app as partner

app = Flask(__name__)

app.register_blueprint(contract)
app.register_blueprint(order)
app.register_blueprint(partner)

CORS(app, automatic_options=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
