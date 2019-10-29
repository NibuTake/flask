from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)

import json
import plotly

import numpy as np
import scipy.stats as stats


def make_graph_data(x, y):
    graphs = [
        dict(
            data=[
                dict(
                    x=x,
                    y=y,
                    type='scatter'
                ),
            ],
            layout=dict(
                title='Interactive Gaussian',
                xaxis=dict(range=[min(x), max(x)])
            )
        )
    ]
    return graphs

N = 1
ids = ['graph-{}'.format(i) for i, _ in enumerate([N])]

# API for calculation.
@app.route('/_calc_dist')
def calc_dist():
    # Make Gaussian data.
    mean = request.args.get('mean', 0, type=float)
    var = request.args.get('var', 0, type=float)
    x = np.linspace(mean - 10, mean + 10, 1000)
    y = stats.norm.pdf(x=x, loc=mean, scale=np.sqrt(var))
    graphs = make_graph_data(x, y)

    # Convert data to json
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]
    return jsonify(graphJ=graphJSON, ids=ids)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', ids=ids)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=18888, threaded=True)
