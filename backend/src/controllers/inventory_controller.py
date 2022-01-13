from flask import Blueprint


from models import db

router = Blueprint("inventory", __name__)


@router.route("/inventory")
def index():
    return "Inventory"
