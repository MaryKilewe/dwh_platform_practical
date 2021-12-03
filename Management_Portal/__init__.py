from flask import Flask


# Initialise the Flask App
app = Flask(__name__)

app.config['SECRET_KEY'] = b'_5#y2L"chhjfgQ8555330002F45687824bdlaqyx42z\n\xec]/>?@$'

from Management_Portal.routes import routes_blueprint
from Management_Portal.data_statistics.charts_stats import statistics_blueprint

app.register_blueprint(routes_blueprint)
app.register_blueprint(statistics_blueprint)