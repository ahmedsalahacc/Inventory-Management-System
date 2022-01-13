from flask import Blueprint


from models import db

router = Blueprint("warehouse", __name__)


@router.route("/warehouse")
def index():
    return "Warehouse"
