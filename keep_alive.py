# Import the Flask framework to create a simple web server
from flask import Flask
# Import the Thread class from the threading module to run the server in a separate thread
from threading import Thread

# Create a Flask app with the name 'app'
app = Flask('')

# Define a route for the root URL ('/') that returns a message indicating the app is alive
@app.route('/')
def home():
    return "Hello. I am alive!"

# Define a function 'run' to start the Flask app
def run():
    # Run the app on all available network interfaces (0.0.0.0) and port 8080
    app.run(host='0.0.0.0', port=8080)

# Define a function 'keep_alive' to start the web server in a separate thread
def keep_alive():
    # Create a new thread and provide the 'run' function as the target
    t = Thread(target=run)
    # Start the thread to run the web server
    t.start()
