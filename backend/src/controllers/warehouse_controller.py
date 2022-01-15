from flask import Blueprint


router = Blueprint("warehouse", __name__)


@router.route("/warehouse")
def index():
    return "Warehouse"
