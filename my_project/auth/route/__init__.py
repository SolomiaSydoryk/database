from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .address_route import address_bp
    from .commercials_route import commercials_bp
    # from .employee_route import employee_bp
    from .interactive_advertising_panel_route import interactive_advertising_panel_bp
    from .manufacturer_route import manufacturer_bp
    # from .owner_route import owner_bp
    from .section_route import section_bp
    from .specifications_route import specifications_bp
    from .supermarket_route import supermarket_bp

    app.register_blueprint(address_bp)
    app.register_blueprint(commercials_bp)
    # app.register_blueprint(employee_bp)
    app.register_blueprint(interactive_advertising_panel_bp)
    app.register_blueprint(manufacturer_bp)
    # app.register_blueprint(owner_bp)
    app.register_blueprint(section_bp)
    app.register_blueprint(specifications_bp)
    app.register_blueprint(supermarket_bp)
