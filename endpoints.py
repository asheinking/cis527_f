#endpoints.py
from flask import Flask, render_template, stream_with_context
import time

app = Flask(__name__)


@app.route('/api/landing')
def get_landing_page():
    return render_template('landing_page.html', variable='API V2')

@app.route('/api/work')
def perform_infinite_work():
    def generate():
        start_time = time.time()

        # Simulate processing time without printing intermediate steps
        call_range()
        call_range()
        call_range()
        call_range()
        call_range()
        call_range()
        call_range()
        call_range()

        total_time = time.time() - start_time
        print(total_time)
        yield f"Finished. Total Elapsed Time: {total_time:.2f} seconds\n"

    def call_range():
        result = 0
        for i in range(50000000):
            result += i
        for i in range(50000000):
            result += i

        
    return app.response_class(generate(), mimetype='text/plain')

if __name__ == "__main__":
    # Change host to '0.0.0.0' to bind to all network interfaces
    app.run(host='0.0.0.0', port=5000, threaded=False)