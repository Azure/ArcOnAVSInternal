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
        files_to_upload = ['config.json','debug_infra.yaml','.temp/vmware-appliance.yaml', '.temp/vmware-infra.yaml',
        '.temp/vmware-resource.yaml', '.temp/kubeconfig', 'console_output.txt', os.path.join(self.kva_log_dir, 'kva.log')]
        dirs_to_upload = ['logs']
        files_not_found = []
        dirs_not_found = []
        
        for log_file in files_to_upload:
            if os.path.isfile(log_file):    
                shutil.copy(log_file, self.logs_folder)
            else:
                files_not_found.append(log_file)

        for log_dir in dirs_to_upload:
            if os.path.isdir(log_dir):
                shutil.copytree(log_dir, self.logs_folder + '/' + log_dir)
            else:
                dirs_not_found.append(log_dir)
        
        if len(files_not_found)!=0 or len(dirs_not_found)!=0:
            logging.error('following files/directories not found: {},{}'.format(files_not_found,dirs_not_found))

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