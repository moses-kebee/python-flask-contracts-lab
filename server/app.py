#!/usr/bin/env python3
from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"},
]
customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)


@app.route("/contract/<int:id>")
def contract_by_id(id):
    # Look for a contract dict whose "id" matches the id from the URL
    contract = next((c for c in contracts if c["id"] == id), None)

    if contract:
        # 200: found — return the contract text
        return make_response(contract["contract_information"], 200)
    else:
        # 404: no contract with that id
        return make_response("Contract not found", 404)


@app.route("/customer/<string:customer_name>")
def customer_by_name(customer_name):
    # Only confirm existence — never expose customer data
    if customer_name in customers:
        # 204: found, no content
        return make_response("", 204)
    else:
        # 404: customer doesn't exist
        return make_response("Customer not found", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)