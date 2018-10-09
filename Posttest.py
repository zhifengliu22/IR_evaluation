import requests
import json


def ir_evaluation_test():
    url = "http://127.0.0.1:5000/evaluation/"
    data = {"y_true": [1, 2, 3, 4, 5], "y_pred": [1, 4, 5, 9, 20]}
    headers = {"Content-Type": "application/json"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(r.text)


if __name__ == "__main__":
    ir_evaluation_test()