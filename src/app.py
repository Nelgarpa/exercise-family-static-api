from flask import Flask, jsonify, request
from flask_cors import CORS
from datastructure import FamilyStructure

app = Flask(__name__)
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.route("/members", methods=["GET"])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

@app.route("/members", methods=["POST"])
def add_member():
    try:
        member_data = request.get_json()
        if not member_data or "first_name" not in member_data or "age" not in member_data or "lucky_numbers" not in member_data:
            return jsonify({"error": "Missing data"}), 400
        jackson_family.add_member(member_data)
        return jsonify({"message": "Member added successfully"}), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)
    if deleted:
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
