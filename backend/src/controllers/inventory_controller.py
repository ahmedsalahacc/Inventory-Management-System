from flask import Blueprint


router = Blueprint("inventory", __name__)


@router.route("/inventory")
def index():
    return "Inventory"
