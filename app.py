"""
TODO Stage 1: 
    Make a positive/negative/neutral scoring fot individual tweets
    Create a pipeline which allows tweets to directly be accessed via an API
    
"""
from flask import Flask, jsonify, request
import sentiment
import asyncio
import twikit

app = Flask(__name__)

analyzer = sentiment.Analyzer()

@app.route("/query", methods=["GET"])
def query():
    query = request.args.get('q')
    # print(query)
    response = jsonify(analyzer.process_tweet(query))
    # response = jsonify({"query": f"ur query is {query}"})
    # print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)