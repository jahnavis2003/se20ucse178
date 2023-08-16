from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fetch_numbers(url):
    try:
        response = requests.get(url, timeout=0.5)
        data = response.json()
        return data.get("numbers", [])
    except (requests.exceptions.RequestException, ValueError):
        return []

def merge_unique_sorted(numbers_lists):
    merged_numbers = sorted(set(number for numbers in numbers_lists for number in numbers))
    return merged_numbers

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')

    numbers_lists = [fetch_numbers(url) for url in urls]

    merged_numbers = merge_unique_sorted(numbers_lists)

    return jsonify({"numbers": merged_numbers})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)

