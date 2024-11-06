from flask import Blueprint, render_template, send_file , url_for, redirect, request, jsonify, session
from facades.vacation_facade import VacationFacade
from utils.image_handler import ImageHandler
from models.client_error import *
from facades.auth_facade import AuthFacade
from utils.logger import Logger
from facades.likes_facade import *
from models.role_model import RoleModel

vacation_blueprint = Blueprint("vacations_view",__name__)
facade = VacationFacade()
auth_facade = AuthFacade()
likes_facade = LikesFacade()


@vacation_blueprint.route("/vacations")
def list():
    try:
        auth_facade.block_anonymous()
        all_vacations = facade.get_all_vacations()
        current_user = session.get("current_user")
        liked_vacations = likes_facade.user_Likes_per_vacation(current_user["userId"])
        return render_template("vacations.html",vacations = all_vacations,likes = liked_vacations, active="vacations",user=RoleModel.User.value)
        
    except AuthError as err:
        return redirect(url_for("auth_view.login",error=err.message))
    except ValidationError as err:
        return render_template("login.html", error=err.message)


@vacation_blueprint.route("/vacations/images/<string:vacation_picture_file>")
def get_image(vacation_picture_file):
    image_path = ImageHandler.get_image_path(vacation_picture_file)
    return send_file(image_path)


@vacation_blueprint.route("/vacations/new", methods = ["GET","POST"])
def insert():
    try:
        auth_facade.block_non_admin()
        if(request.method=="GET"): return render_template("insert.html", active="new")
        facade.add_new_holiday()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        redirect("auth_view.login",error=err.message, credentials = {})
    except ValidationError as err:
        return render_template("insert.html", error=err.message)


@vacation_blueprint.route("/vacations/edit/<int:vacation_id>", methods = ["GET","POST"])
def edit(vacation_id):
    try:
        auth_facade.block_non_admin()
        if(request.method=="GET"): 
            one_vacation = facade.get_one_vacation(vacation_id)
            return render_template("edit.html", vacation = one_vacation)
    
        facade.update_vacation()
        return redirect(url_for("vacations_view.list"))
    except ValidationError as err:
        return render_template("edit.html", error=err.message) 

@vacation_blueprint.route("/vacations/delete/<int:vacation_id>")
def delete(vacation_id):
    try:
        auth_facade.block_non_admin()
        facade.delete_existing_vacation(vacation_id)
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        all_vacations = facade.get_all_vacations()
        return render_template("home.html",error = err.message, vacations = all_vacations,admin=1)
    

@vacation_blueprint.route("/vacations/like_vacation/<int:vacation_id>", methods=["POST"])
def like_vacation(vacation_id):
    current_user = session.get("current_user")
    likes_facade.add_likes_to_vacations(current_user["userId"], vacation_id)
    new_like_count = likes_facade.get_likes_by_vacation_id(vacation_id)  # Fetch the updated like count
    return jsonify({"success": True, "message": "Liked vacation", "LikeCount": new_like_count}), 200


@vacation_blueprint.route("/vacations/unlike_vacation/<int:vacation_id>", methods=["POST"])
def unlike_vacation(vacation_id):
    current_user = session.get("current_user")
    likes_facade.remove_like_from_vacation(current_user["userId"], vacation_id)
    new_like_count = likes_facade.get_likes_by_vacation_id(vacation_id)  # Fetch the updated like count
    return jsonify({"success": True, "message": "Unliked vacation", "LikeCount": new_like_count}), 200