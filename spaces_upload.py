import boto3
from dotenv import load_dotenv
import os


def upload_to_space(file_name, space_name, folder):
    '''Uploads file_name to digital ocean.
    file_name must be a file path to a file on the system.'''

    # set environment variables
    load_dotenv()

    # access environment variables
    key = os.getenv("DO_ACCESS_KEY")
    secret = os.getenv("DO_SECRET_KEY")

    
    # Extract file name from file path given
    my_file_name = os.path.basename(file_name)

    # remove leading slash from upload folder name
    if folder[0] == "/" and folder != '':
        folder = folder[1:]

    # Initialize a session using Spaces
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='sgp1',
                            endpoint_url='https://sgp1.digitaloceanspaces.com',
                            aws_access_key_id=key,
                            aws_secret_access_key=secret)

    if folder:
        client.upload_file(file_name, space_name, os.path.join(folder, my_file_name))
    else:
        client.upload_file(file_name, space_name, my_file_name)

    print("Uploaded {} to Digital Ocean in folder {}".format(my_file_name, folder))

    return None


if __name__ == "__main__":
    upload_to_space()
