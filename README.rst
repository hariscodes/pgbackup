pgbackup
========

CLI for backing up remote PostgreSQL database either locally or to S3.

Usage
-----

Pass in a full database URL, the storage driver, and the destination.

* URL Format should be "postgres://**<username>**:**<password>@<database-server>**:**<port>**/**<database-name>**"
* Specify driver with `--driver` or `-d`; **MUST** be "s3" or "local"
* Specify destination with S3 bucket name or local file path

S3 example w/ bucket name:
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ pgbackup postgres://foo:bar@example.com:5432/dbname --driver s3 my_backup_bucket

This will result in a SQL file with the database name and timestamp in your S3 bucket.

Local example w/ file name:
^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    $ pgbackup postgres://foo:bar@example.com:5432/dbname --driver local /var/local/dbname/backups/dump.sql
