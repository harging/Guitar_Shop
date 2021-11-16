from flask import Flask, render_template

from controllers.items_controller import items_blueprint
from controllers.brands_controller import brands_blueprint

app = Flask(__name__)

app.register_blueprint(items_blueprint)
app.register_blueprint(brands_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)