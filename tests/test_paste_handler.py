from flask import url_for
from time import time

from yaml import load
from pb.pb import create_app
from pb.paste.handler import render

def test_paste_render():
    app = create_app()

    rv = app.test_client().post('/', data=dict(
        c = str(time())
    ))

    data = load(rv.get_data())
    with app.test_request_context():
        url = url_for('paste.get', handler='r', label=data['short'])

    rv = app.test_client().get(url)
    assert rv.status_code == 200

def test_markdown_render_uses_document_styles() -> None:
    """Markdown renders in the scoped document wrapper with table support."""
    app = create_app()
    source = b'| Header | Value |\n| --- | --- |\n| First | Second |\n'

    with app.test_request_context():
        content = render(source, 'text/x-markdown')

    assert '<article class="markdown-body">' in content
    assert '/static/css/markdown.css' in content
    assert '<table>' in content
