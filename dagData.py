from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_dag_data')
def get_dag_data():
    dag_data = {
        "nodes": [
            { "id": "A", "type": "TYPE_1" },
            { "id": "B", "type": "TYPE_2" },
            { "id": "C", "type": "TYPE_3" },
            { "id": "D", "type": "TYPE_4" },
            { "id": "E", "type": "TYPE_1" }
        ],
        "links": [
            { "source": "A", "target": "B" },
            { "source": "A", "target": "C" },
            { "source": "B", "target": "D" },
            { "source": "C", "target": "D" },
            { "source": "D", "target": "E" }
        ]
    }
    return jsonify(dag_data)

if __name__ == '__main__':
    app.run(debug=True)