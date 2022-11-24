import logging
import pathlib
import json

from pkgs._exceptions import AzCommandError
from pkgs._az_cli import az_cli
 
class UploadLogs:

    def __init__(self, storage_account):
        self.storage_account = storage_account

    def container_exists(self, container_name):
        res, err = az_cli('storage', 'container', 'exists', 
                        '--account-name', f'"{self.storage_account}"',
                        '--name', f'"{container_name}"',
                        '--auth-mode','key')
        if err:
            raise AzCommandError('failed to get container details')

        container_details = json.loads(res)
        return container_details["exists"]
    
    def create_container(self, container_name):
        res, err = az_cli('storage', 'container', 'create', 
                        '--name', f'"{container_name}"',
                        '--account-name', f'"{self.storage_account}"',
                        '--public-access', 'blob',
                        '--auth-mode','key')
        if err:
            raise AzCommandError('failed to create container')

    def upload_folder_to_storage(self, logs_folder, container_name):  
        if(not self.container_exists(container_name)):
            self.create_container(container_name)
        path = pathlib.PurePath(logs_folder)

        res, err = az_cli('storage', 'blob', 'upload-batch', 
                        '--destination', f'"{container_name}"',
                        '--account-name', f'"{self.storage_account}"',
                        '--source', f'"{logs_folder}"',
                        '--destination-path', f'"{path.name}"',
                        '--auth-mode','key')
        if err:
            raise AzCommandError('failed to upload files to container')
        logging.info("uploaded files to container")
