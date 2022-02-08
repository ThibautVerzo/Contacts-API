"""ContactsAPI commands file."""
from contactsapi import create_app

import click


def run():
    app = create_app()
    app.run()
