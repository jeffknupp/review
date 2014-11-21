from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask

from review import app


def main():
    """Main entry point for script."""
    app.config['DEBUG'] = True
    app.testing = True
    app.run(debug=True)


if __name__ == '__main__':
    import sys
    sys.exit(main())
