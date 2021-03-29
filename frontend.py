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
                    [5.0, 5.68],
                ],
                "stats": {
                    "fit": [],
                    "error": 5,
                    "func": ""
                }
            }
        )
    elif viz_type == 'simplescatterwithdate':
        data_format_one = {
            "name": "simple scatter plotting with date",
            "data_x": [
                '2021-01-02',
                '2021-01-03',
                '2021-01-04',
                '2021-01-05',
                '2021-01-06',
                '2021-01-07',
                '2021-01-08',
                '2021-01-09',
                '2021-01-10',
                '2021-01-11',
                '2021-01-12'
            ],
            "data_y": [
                10.0,
                8.04,
                13.0,
                7.58,
                6.0,
                7.24,
                7.0,
                4.82,
                12.0,
                10.84
            ],
        }
        return jsonify(data_format_one)
    elif viz_type == 'partitionscatter':
        data_format_one = {
            "name": "simple scatter plotting with date",
            "data_x": [
                '2021-01-02',
                '2021-01-03',
                '2021-01-04',
                '2021-01-05',
                '2021-01-06',
                '2021-01-07',
                '2021-01-08',
                '2021-01-09',
                '2021-01-10',
                '2021-01-11',
                '2021-01-12'
            ],
            "data_y": [
                10.0,
                8.04,
                13.0,
                7.58,
                6.0,
                7.24,
                7.0,
                4.82,
                12.0,
                10.84
            ],
        }
        return jsonify(data_format_one)
    elif viz_type == 'regionalcomp':
        return jsonify()
    else:
        return jsonify()


if __name__ == '__main__':
    app.run()
