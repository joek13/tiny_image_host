"""Exposes the main application for use by a production WSGI server."""

from tinyimg import create_app

application = create_app()
