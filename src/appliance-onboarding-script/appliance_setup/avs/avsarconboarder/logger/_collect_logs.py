import logging
import os
import shutil 
import datetime

from pkgs._az_cli import az_cli
from pkgs._exceptions import AzCommandError
from ..constants import Constant

class CollectLogs:

    def __init__(self, logs_dir, config):
        os.makedirs(logs_dir)
        self.logs_dir = logs_dir
        self.__config = config
        self.kva_log_dir = "C:\ProgramData\kva"   

    def fetch_onboardinglogs(self):
        script_dir = os.path.join(Constant.ROOT_DIR, 'src/appliance-onboarding-script')
        shutil.copy(os.path.join(script_dir, 'config.json'), self.logs_dir)
        shutil.copy(os.path.join(script_dir, '.temp/vmware-appliance.yaml'), self.logs_dir)
        shutil.copy(os.path.join(script_dir, '.temp/vmware-infra.yaml'), self.logs_dir)
        shutil.copy(os.path.join(script_dir, '.temp/vmware-resource.yaml'), self.logs_dir)
        shutil.copy(os.path.join(script_dir, '.temp/kubeconfig'), self.logs_dir)
        shutil.copy(os.path.join(script_dir, 'output.txt'), self.logs_dir) 
        shutil.copytree(os.path.join(script_dir, 'logs'), self.logs_dir)
        shutil.copy(os.path.join(self.kva_log_dir, 'kva.log'), self.logs_dir)
    
    def fetch_arc_appliance_logs(self):
        arc_appliance_ip = self.__config["applianceControlPlaneIpAddress"]
        vcenter_ip = self.__config['vCenterFQDN']
        vcenter_username = self.__config['vCenterUserName']
        vcenter_password = self.__config['vCenterPassword']
        res, err = az_cli('arcappliance', 'logs', 'vmware', 
                        '--ip', arc_appliance_ip,
                        '--address', vcenter_ip,
                        '--username', vcenter_username,
                        '--password', vcenter_password)
        if err:
            raise AzCommandError('error in fetching arc appliance logs fetched')
        logging.info("arc appliance logs fetched")

        arc_appl_log_file = open(os.path.join(self.logs_dir,'arc_appl_log_file.txt'), 'w')
        arc_appl_log_file.write(res)