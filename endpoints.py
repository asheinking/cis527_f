from flask import Flask, render_template
from flask_socketio import SocketIO
import time

app = Flask(__name__)


@app.route('/api/landing')
def get_landing_page():
    return render_template('landing_page.html', variable='Hello, World!')

@app.route('/api/work')
def perform_infinite_work():
    for _ in range(1000):
        time.sleep(0.1)  # Simulate some processing time
    return "finished. JK! that is impossible"

if __name__ == "__main__":
    # Change host to '0.0.0.0' to bind to all network interfaces
    app.run(host='0.0.0.0', port=5000, threaded=False)