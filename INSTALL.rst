Installation
============

DARIAH-repository docker installation (local installation)
-------------------

Requirements
~~~~~~~~~~~~~~~~~~~
DARIAH-repository is a forked github project from `ZENODO <https://github.com/zenodo/zenodo>` and depends on PostgreSQL, Elasticsearch 2.x, Redis and RabbitMQ.

If you are only interested in running DARIAH-repository locally, follow the Docker
installation guide below.

For this guide you will need to install
`docker <https://docs.docker.com/engine/installation/>`_ along with the
`docker-compose <https://docs.docker.com/compose/>`_ tool.

Docker installation is not necessary, although highly recommended.

Docker installation
~~~~~~~~~~~~~~~~~~~
The easiest way to get started with DARIAH repository is using the pre-defined docker images (https://hub.docker.com/r/indigodatacloudapps/dariah-repository/) and provided ``docker-compose`` file. The installation requires only two steps, first checkout the source code and then boot them up using Docker Compose:
We presume that all installation is done in the home directory (``~`` in Linux based systems).

.. code-block:: console

    $ cd ~
    $ git clone https://github.com/indigo-dc/dariah-repository.git
    $ cd ~/dariah-repository/
    $ git checkout master
    $ docker-compose up

Keep the session with the docker-compose above alive, and in a new shell
run the init script which creates the database tables, search indexes
and some data fixtures:

.. code-block:: console

    $ cd ~/dariah-repository
    $ docker-compose run --rm statsd bash /init.sh

Next, load the demo records and index them:

.. code-block:: console

    $ docker-compose run --rm web zenodo fixtures loaddemorecords
    $ docker-compose run --rm web zenodo migration recordsrun
    $ docker-compose run --rm web zenodo migration reindex -t recid
    $ docker-compose run --rm web zenodo index run -d

Now visit the following URL in your browser:

.. code-block:: console

    https://<docker ip>

.. note::

    If you're running docker on Linux or newer Mac OSX systems,
    the ``<docker ip>`` is usually the localhost. For older Mac OSX and Windows
    systems running docker through ``docker-machine``, you can find the IP with

    .. code-block:: console

        $ docker-machine ip <machine-name>

You can use the following web interface to inspect Elasticsearch and RabbitMQ:

- Elasticsearch: http://<docker ip>:9200/_plugin/hq/
- RabbitMQ: http://<docker ip>:15672/ (guest/guest)
- HAProxy: http://<docker ip>:8080/ (guest/guest)

Also the following ports are exposed on the Docker host:

- ``80``: HAProxy
- ``81``: Nginx
- ``443``: HAProxy
- ``444``: Nginx
- ``5000``: dariah-repository
- ``5432``: PostgreSQL
- ``5601``: Kibana
- ``5672``: RabbitMQ
- ``6379``: Redis
- ``8080``: HAProxy stats
- ``8125``: StatsD (UDP)
- ``9200``: Elasticsearch
- ``9300``: Elasticsearch
- ``15672``: RabbitMQ management console

