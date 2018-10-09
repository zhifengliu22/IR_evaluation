# coding = utf-8
from flask import Flask, request
from ir_metrics import to_relevance_scores, precision_at_k, recall, f_measure, avg_precision_at_k, dcg, ndcg
from flask_cors import *
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/evaluation/", methods=["POST", "GET"])
def ir_evaluation():
    if request.method == "POST":
        json_dict = request.get_json()
        y_true = json_dict["y_true"]
        y_pred = json_dict["y_pred"]
        rel_scores = to_relevance_scores(y_true, y_pred)

        p_5 = precision_at_k(y_true, y_pred, k=5)
        p_10 = precision_at_k(y_true, y_pred, k=10)
        p_20 = precision_at_k(y_true, y_pred, k=20)

        _recall = recall(y_true, y_pred)

        f = f_measure(y_true, y_pred)

        avg_prec = avg_precision_at_k(y_true, y_pred)

        # _dcg = dcg(y_true, y_pred)

        ndcg_5 = ndcg(y_true, y_pred, k=5)
        ndcg_10 = ndcg(y_true, y_pred, k=10)
        ndcg_20 = ndcg(y_true, y_pred, k=20)

        evaluation_result = {"success": "true", "rel_scores": rel_scores, "p@5": p_5, "p@10": p_10, "p@20": p_20,
                             "recall": _recall, "F值": f,
                             "AP值": avg_prec,
                             "NGDC@5": ndcg_5, "NGDC@10": ndcg_10, "NGDC@20": ndcg_20}
        evaluation_results = json.dumps(evaluation_result, ensure_ascii=False)
        return evaluation_results
    else:
        return """<html><dody>
        Something went horribly wrong
        </body></html>"""


if __name__ == "__main__":
    app.run(debug=True, port=5000)