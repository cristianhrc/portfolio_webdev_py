from flask import Flask
import os
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        # SENDGRID_KEY = os.environ.get('SENDGRID_API_KEY'),
        # SENDGRID_KEY = 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
    )

    from . import portfolio

    app.register_blueprint(portfolio.bp)

    return app

app = create_app()
if __name__ == '__main__':
    app.run()
