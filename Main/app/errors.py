from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.route("/errors/400", methods=["GET"])
def HTTP400():
    return render_template('errors/400.html')

@errors.route("/errors/401", methods=["GET"])
def HTTP401():
    return render_template("errors/401.html")

@errors.route("/errors/403", methods=["GET"])
def HTTP403():
    return render_template("errors/403.html")

@errors.route("/errors/404", methods=["GET"])
def HTTP404():
    return render_template("errors/404.html")

@errors.route("/errors/418", methods=["GET"])
def HTTP418():
    return render_template("errors/418.html")

@errors.route("/errors/500", methods=["GET"])
def HTTP500():
    return render_template("errors/500.html")


def error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        return render_template('errors/400.html'), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return render_template('errors/401.html'), 401
    
    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(418)
    def I_am_a_teapot(error):
        return render_template('errors/418.html'), 418
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html'), 500