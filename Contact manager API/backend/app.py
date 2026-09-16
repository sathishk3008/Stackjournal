from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

FILE_PATH = "backend/contacts.json"


@app.route("/contacts", methods=["GET"])
def get_contacts():
    with open(FILE_PATH, "r") as file:
        contacts = json.load(file)

    return jsonify(contacts)


@app.route("/contacts", methods=["POST"])
def add_contact():

    new_contact = request.get_json()

    with open(FILE_PATH, "r") as file:
        contacts = json.load(file)

    contacts.append(new_contact)

    with open(FILE_PATH, "w") as file:
        json.dump(contacts, file, indent=4)

    return jsonify({"message": "Contact added successfully"})


@app.route("/contacts/<int:id>", methods=["PUT"])
def update_contact(id):

    updated_contact = request.get_json()

    with open(FILE_PATH, "r") as file:
        contacts = json.load(file)

    for contact in contacts:
        if contact["id"] == id:
            contact["name"] = updated_contact["name"]
            contact["email"] = updated_contact["email"]
            contact["phone no"] = updated_contact["phone no"]

    with open(FILE_PATH, "w") as file:
        json.dump(contacts, file, indent=4)

    return jsonify({"message": "Contact updated successfully"})


@app.route("/contacts/<int:id>", methods=["DELETE"])
def delete_contact(id):

    with open(FILE_PATH, "r") as file:
        contacts = json.load(file)

    contacts = [contact for contact in contacts if contact["id"] != id]

    with open(FILE_PATH, "w") as file:
        json.dump(contacts, file, indent=4)

    return jsonify({"message": "Contact deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)