from argparse import Action, ArgumentParser

known_drivers = ['local','s3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error('Error: Unknown Driver, available drivers are "local" and "s3"')
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help='URL of the postgres database to backup')
    parser.add_argument('--driver', '-d',
            help='how and where to store the backup',
            nargs=2,
            metavar=('driver','destination'),
            action=DriverAction,
            required=True)
    return parser

def main():
    import boto3
    import time
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    try:
        dump = pgdump.dump(args.url)
    except OSError as err:
        print('ERROR: ErrorOnDump: {err}')

    if args.driver == 's3':
        client = boto3.client('s3')
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        file_name = pgdump.dump_file_name(args.url, timestamp)
        try:
            storage.s3(client,dump.stdout,args.destination,file_name)
            print(f'Backing up database to {args.destination} on S3 as {file_name}')
        except:
            print(f'ERROR: ErrorOnS3Dump: No such bucket')
    else:
        outfile = open(args.destination,'wb')
        print(f'Backing up database to {args.destination} on local storage as {file_name}')
        storage.local(dump.stdout,outfile)
