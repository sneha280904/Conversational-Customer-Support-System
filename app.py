from flask import Flask, request, jsonify, render_template
from chatbot import handle_query
from database import init_db, log_session  # Removed fetch_history import

app = Flask(_name_)
init_db()  # Initialize database

@app.route('/')
def index():
    return render_template('index.html')  # Render chatbot UI

@app.route('/query', methods=['POST'])
def query():
    try:
        user_id = request.json.get('user_id')
        user_message = request.json.get('message')

        # Process user query
        bot_response = handle_query(user_message)

        # Log the session
        log_session(user_id, user_message, bot_response)

        return jsonify({'response': bot_response})
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({'error': str(e)}), 500

if _name_ == '_main_':
    app.run(debug=True)