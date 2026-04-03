from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import config

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    from app.routes.main        import main_bp
    from app.routes.communes    import communes_bp
    from app.routes.stations    import stations_bp
    from app.routes.fosses      import fosses_bp
    from app.routes.eaux        import eaux_bp
    from app.routes.vehicules   import vehicules_bp
    from app.routes.menages     import menages_bp
    from app.routes.chauffeurs  import chauffeurs_bp
    from app.routes.personnels  import personnels_bp
    from app.routes.equipements import equipements_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(communes_bp,    url_prefix="/communes")
    app.register_blueprint(stations_bp,    url_prefix="/stations")
    app.register_blueprint(fosses_bp,      url_prefix="/fosses")
    app.register_blueprint(eaux_bp,        url_prefix="/eaux")
    app.register_blueprint(vehicules_bp,   url_prefix="/vehicules")
    app.register_blueprint(menages_bp,     url_prefix="/menages")
    app.register_blueprint(chauffeurs_bp,  url_prefix="/chauffeurs")
    app.register_blueprint(personnels_bp,  url_prefix="/personnels")
    app.register_blueprint(equipements_bp, url_prefix="/equipements")

    return app
