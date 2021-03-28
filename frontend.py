from flask import Flask, jsonify, render_template


app = Flask("simple-viz")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getdata/<string:viz_type>')
def get_data(viz_type):
    if viz_type == 'linreg':
        return jsonify(
            {
                "name": "linear regression plotting",
                "data": [
                    [10.0, 8.04],
                    [8.0, 6.95],
                    [13.0, 7.58],
                    [9.0, 8.81],
                    [11.0, 8.33],
                    [14.0, 9.96],
                    [6.0, 7.24],
                    [4.0, 4.26],
                    [12.0, 10.84],
                    [7.0, 4.82],
                    [5.0, 5.68]
                ],
                "stats": {
                    "fit": [],
                    "error": 5,
                    "func": ""
                }
            }
        )
    elif viz_type == 'simplescatter':
        return jsonify()
    elif viz_type == 'partitionscatter':
        return jsonify()
    elif viz_type == 'regionalcomp':
        return jsonify()
    else:
        return jsonify()


if __name__ == '__main__':
    app.run()
