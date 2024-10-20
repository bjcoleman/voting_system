
from flask import Flask, jsonify, request, render_template
import json
from memory_votes import MemoryVotes

app = Flask(__name__)
votes = MemoryVotes()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results')
def results():
    return jsonify(votes.get_votes())


@app.route('/vote', methods=['POST'])
def vote():
    data = json.loads(request.data)

    if 'vote' not in data:
        return 'Invalid body', 400

    the_vote = data['vote']

    if not votes.is_valid_vote(the_vote):
        return 'Invalid vote', 400

    votes.register_vote(the_vote)

    return jsonify(votes.get_votes())


if __name__ == '__main__':
    app.run(port=8000, debug=True)
