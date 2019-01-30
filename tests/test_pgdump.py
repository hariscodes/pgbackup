import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
    '''
    Utilized pg_dump with db URL
    '''

    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump',url],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

def test_dump_handles_os_error(mocker):
    '''
    If pg_backup not installed on machine, pg_dump will throw FileNotFoundError
    '''

    mocker.patch('subprocess.Popen', side_effect=OSError('No such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)

def test_dump_file_name_without_timestamp():
    '''
    pgdump.dump_file_name returns the name of the database
    '''
    assert pgdump.dump_file_name(url) == 'db_one.sql'

def test_dump_file_name_with_timestamp():
    '''
    pgdump.dump_file_name returns the name of the database with timestamp
    '''
    timestamp = '2018-01-29T12:00:00'
    assert pgdump.dump_file_name(url, timestamp) == f'db_one-{timestamp}.sql'


