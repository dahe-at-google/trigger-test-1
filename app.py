import os
import sys

from flask import Flask
import impl


app = Flask(__name__)


@app.route('/')
def root():
    return impl.hello_world()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
