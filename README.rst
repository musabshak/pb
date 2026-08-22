==
pb
==

``pb`` is a lightweight pastebin (and url shortener) built using
`flask <http://flask.pocoo.org/docs/0.10/quickstart/>`_.

This project was forked from `ptpb.pw
<https://ptpb.pw>`_ and is currently live in the Arista infra.

Building the docker image & running locally
-------------------------------------------

Run the following in your shell:

.. code:: shell-session

    $ cp config.yaml.example config.yaml
    $ docker build -t pb .
    $ docker run -p 10002:10002 -v/tmp/pb:/data/db -t pb

Then access http://127.0.0.1:10002 on your browser.

Local Markdown renderer development
-----------------------------------

The development Compose stack starts an isolated MongoDB instance and serves pb at
``http://127.0.0.1:10002``. It never uses the production MongoDB configuration.

.. code:: shell-session

    $ docker compose -f compose.dev.yaml up --build

In another terminal, create the Markdown showcase paste:

.. code:: shell-session

    $ ./dev/seed-markdown-showcase.sh
    Open http://localhost:10002/r/<id>.md

The app watches the mounted Markdown renderer, templates, and ``run.py`` files. Refresh the showcase
URL after changing them. Stop the stack with ``docker compose -f compose.dev.yaml down``. Use
``docker compose -f compose.dev.yaml down -v`` only when the local test database can be discarded.
