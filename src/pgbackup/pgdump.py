import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url,timestamp=None):
    file_name = url.split('/')[-1].split('?')[0]
    if timestamp:
        return f'{file_name}-{timestamp}.sql'
    else:
        return f'{file_name}.sql'
