from tests import Chatbot, check_grammar
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send-message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    res = check_grammar(user_message)
    return jsonify({'reply': chat_bot.generate_answer(check_grammar(res[0])), 'check': res[1]})


if __name__ == '__main__':
    chat_bot = Chatbot()
    app.run(debug=True)