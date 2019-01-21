pgbackup
========

CLI for backing up remote PostgreSQL database either locally or to S3.

Preparing for development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:hariscodes/pgbackup``
3. ``cd`` into the repository.
4. Fetch development dependencies: ``make install``
5. Activate virtualenv: ``pipenv shell``


Usage
-----

Pass in a full database URL, the storage driver, and the destination.

S3 example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/dbname --driver s3 my_backup_bucket

::

    $ pgbackup postgres://bob@example.com:5432/dbname --driver local /var/local/dbname/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active, then use:

::

    $ pipenv run make
