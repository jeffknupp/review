from review import app


def get_app():
    """Return the application object."""
    return app

if __name__ == '__main__':
    get_app().run(debug=True)
