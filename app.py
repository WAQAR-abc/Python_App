from flask import Flask
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Log the request with an info level message
    app.logger.info('🌐 App endpoint was accessed.')
    return 'Hey DevOps Learner!💫 <br>You are doing great! Keep Learning!✨'

if __name__ == '__main__':
    # This ensures the app listens on all network interfaces inside the container
    app.run(host='0.0.0.0', port=5000)

