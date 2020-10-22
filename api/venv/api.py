import time
from flask import Flask, g
import os
import sqlite3
from flask.json import jsonify

app = Flask(__name__)

# La liga, Premier League, Ligue 1, Serie A, Bundesliga
leagueIDs = [2833, 2790, 2664, 2857, 2755]

def connect_to_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(os.path.abspath('top_scorers.db'))

    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                    for idx, value in enumerate(row))

    db.row_factory = make_dicts

    return db

def execute(query, args=()):
    val = connect_to_db().execute(query, args)
    qr = val.fetchall()
    val.close()
    return qr


@app.route('/laliga')
def laliga_top():
    query = 'SELECT playerName, goals, teamName FROM topScorers WHERE leagueID = 2833 ORDER BY goals desc'
    res = execute(query)
    return jsonify(res)

@app.route('/bundesliga')
def bundesliga_top():
    query = 'SELECT playerName, goals, teamName FROM topScorers WHERE leagueID = 2755 ORDER BY goals desc'
    res = execute(query)
    return jsonify(res)

@app.route('/premierleague')
def premier_top():
    query = 'SELECT playerName, goals, teamName FROM topScorers WHERE leagueID = 2790 ORDER BY goals desc'
    res = execute(query)
    return jsonify(res)

@app.route('/ligue1')
def ligue1_top():
    query = 'SELECT playerName, goals, teamName FROM topScorers WHERE leagueID = 2664 ORDER BY goals desc'
    res = execute(query)
    return jsonify(res)

@app.route('/seriea')
def seriea_top():
    query = 'SELECT playerName, goals, teamName FROM topScorers WHERE leagueID = 2857 ORDER BY goals desc'
    res = execute(query)
    return jsonify(res)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/time')
def get_current_time():
    return {'time': time.time()}

