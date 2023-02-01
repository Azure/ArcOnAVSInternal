import logging
import os
import shutil 
import glob

from pkgs._az_cli import az_cli
from pkgs._utils import safe_escape_characters

class CollectLogs:

    def __init__(self, logs_folder, config):
        os.makedirs(logs_folder)
        self.logs_folder = logs_folder
        self.__config = config
        self.kva_log_dir = "C:\ProgramData\kva"   

    def fetch_onboardinglogs(self):
        try:
            if os.path.isfile('config_avs.json'):
                print("file found")
                shutil.copy('config_avs.json', self.logs_folder)
            if os.path.isfile('.temp/vmware-appliance.yaml'):
                shutil.copy('.temp/vmware-appliance.yaml', self.logs_folder)
            if os.path.isfile('.temp/vmware-infra.yaml'):
                shutil.copy('.temp/vmware-infra.yaml', self.logs_folder)
            if os.path.isfile('.temp/vmware-resource.yaml'):
                shutil.copy('.temp/vmware-resource.yaml', self.logs_folder)
            else:
                print("file not found")
            if os.path.isfile('.temp/kubeconfig'):    
                shutil.copy('.temp/kubeconfig', self.logs_folder)
            if os.path.isfile('console_output.txt'):    
                shutil.copy('console_output.txt', self.logs_folder)
            if os.path.isfile(os.path.join(self.kva_log_dir, 'kva.log')):    
                shutil.copy(os.path.join(self.kva_log_dir, 'kva.log'), self.logs_folder)
            if os.path.isdir('logs'):              
                shutil.copytree('logs', self.logs_folder + '/logs')
        
        except Exception as e:
            logging.error(e)
    
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
            logging.error("failed to fetch arc appliance logs")
        else:
            try:
                files = glob.glob("appliance-logs*")
                shutil.copytree(files[-1], self.logs_folder + '/arc-appliance-logs')
            except Exception as e:
                logging.error(e)