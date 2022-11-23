import logging
import os
import shutil 
import glob

from pkgs._az_cli import az_cli
from pkgs._exceptions import AzCommandError
from pkgs._utils import safe_escape_characters

class CollectLogs:

    def __init__(self, logs_folder, config):
        os.makedirs(logs_folder)
        self.logs_folder = logs_folder
        self.__config = config
        self.kva_log_dir = "C:\ProgramData\kva"   

    def fetch_onboardinglogs(self):
        try:
            shutil.copy('config_avs.json', self.logs_folder)
            shutil.copytree('logs', self.logs_folder + '/logs')
            shutil.copy('.temp/vmware-appliance.yaml', self.logs_folder)
            shutil.copy('.temp/vmware-infra.yaml', self.logs_folder)
            shutil.copy('.temp/vmware-resource.yaml', self.logs_folder)
            shutil.copy('.temp/kubeconfig', self.logs_folder)
            shutil.copy('output.txt', self.logs_folder)
            shutil.copy(os.path.join(self.kva_log_dir, 'kva.log'), self.logs_folder)
        
        except Exception as e:
            logging.info("Insufficient logs captured")
    
    def fetch_arc_appliance_logs(self):
        arc_appliance_ip = self.__config["applianceControlPlaneIpAddress"]
        vcenter_ip = self.__config['vCenterFQDN']
        vcenter_username = self.__config['vCenterUserName']
        vcenter_password = self.__config['vCenterPassword']
        res, err = az_cli('arcappliance', 'logs', 'vmware', 
                        '--ip', f'"{arc_appliance_ip}"',
                        '--address', f'"{vcenter_ip}"',
                        '--username',f'"{vcenter_username}"',
                        '--password="{}"'.format(safe_escape_characters(vcenter_password)))
        if err:
            logging.info("failed to fetch arc appliance logs")
        else:
            logging.info("arc appliance logs fetched")

        try:
            files = glob.glob("appliance-logs*")
            shutil.copytree(files[-1], self.logs_folder + '/arc-appliance-logs')
        except:
            logging.info('appliance-logs folder not found')