"""Solver API routes."""
from flask import Blueprint, request, jsonify
solvers_bp = Blueprint("solvers", __name__)

@solvers_bp.route("/api/v1/solvers", methods=["GET"])
def list_solvers():
    chain = request.args.get("chain", "")
    return jsonify({"solvers": [], "total": 0})

@solvers_bp.route("/api/v1/solvers/top", methods=["GET"])
def top_solvers():
    return jsonify({"solvers": [
        {"address": "0x...", "name": "solver-alpha", "success_rate": 99.8, "fulfilled": 1542},
        {"address": "0x...", "name": "solver-beta", "success_rate": 99.5, "fulfilled": 1298},
    ]})
