import logging
import pathlib

from pkgs._exceptions import AzCommandError
from pkgs._az_cli import az_cli
 
class UploadLogs:

    def __init__(self, storage_account):
        self.storage_account = storage_account

    def container_exists(self, container_name):
        res, err = az_cli('storage', 'container', 'exists', 
                        '--account-name', self.storage_account,
                        '--name', container_name,
                        '--auth-mode','login')
        if err:
            raise AzCommandError('failed to get container details')
        logging.info("container details fetched")
        return res["exists"]
    
    def create_container(self, container_name):
        res, err = az_cli('storage', 'container', 'create', 
                        '--name', container_name,
                        '--account-name', self.storage_account,
                        '--public-access', 'blob',
                        '--auth-mode','login')
        if err:
            raise AzCommandError('failed to create container')
        logging.info("container created")

    def upload_folder_to_storage(self, logs_folder, container_name):  
        if(self.container_exists(container_name) == "false"):
            self.create_container(container_name)
        path = pathlib.PurePath(logs_folder)

        res, err = az_cli('storage', 'blob', 'upload-batch', 
                        '--destination', container_name,
                        '--account-name', self.storage_account,
                        '--source', logs_folder,
                        '--destination-path', path.name,
                        '--public-access', 'blob',
                        '--auth-mode','login')
        if err:
            raise AzCommandError('failed to upload to container')
        logging.info("uploaded files to container")
