#!/usr/bin/python

# These are the exceptions used across different modules.
from common_exceptions import CustomBaseException, ExitCodes

class FilePathNotFoundInArgs(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.CONFIG_NOT_FOUND.value

class AzCommandError(CustomBaseException): 
    def returnExitCode(self):
        exit_code = ExitCodes.GENERIC_ERROR.value
        arc_validate_failure_err = 'arcappliance Validate command failed. Fix the configuration and try again.'
        arc_prepare_failure_err = 'arcappliance prepare command failed.'
        arc_deploy_failure_err = 'arcappliance deploy command failed.'
        arc_create_failure_err = 'arcappliance create command failed.'
        arc_delete_failure_err = 'arcappliance delete command failed.'
        k8s_extn_create_failure_err = 'Create k8s-extension instance failed.'
        k8s_extn_delete_failure_err = 'Delete k8s-extension instance failed.'
        cl_create_failure_err = 'Create Custom Location failed.'
        cl_delete_failure_err = 'Delete Custom Location failed.'
        create_vCenter_err = 'Connect vCenter failed.'
        delete_vCenter_err = 'Delete vCenter failed.'

        if(self.msg.casefold() == arc_validate_failure_err.casefold()):
            return ExitCodes.ARC_APPLIANCE_VALIDATE_FAILURE.value        
        if(self.msg.casefold() == arc_prepare_failure_err.casefold()):
            return ExitCodes.ARC_APPLIANCE_PREPARE_FAILURE.value        
        if(self.msg.casefold() == arc_deploy_failure_err.casefold()):
            return ExitCodes.ARC_APPLIANCE_DEPLOY_FAILURE.value 
              
        if(self.msg.casefold() == arc_create_failure_err.casefold()):
            return ExitCodes.ARC_APPLIANCE_CREATE_FAILURE.value
        if(self.msg.casefold().__contains__(k8s_extn_create_failure_err.casefold())):
            return ExitCodes.K8s_EXTN_CREATE_FAILURE.value
        if(self.msg.casefold() == cl_create_failure_err.casefold()):
            return ExitCodes.CL_CREATE_FAILURE.value    
        if(self.msg.casefold() == create_vCenter_err.casefold()):
            return ExitCodes.VCENTER_CREATE_FAILURE.value                

        if(self.msg.casefold() == arc_delete_failure_err.casefold()):
            return ExitCodes.ARC_APPLIANCE_DELETE_FAILURE.value
        if(self.msg.casefold().__contains__(k8s_extn_delete_failure_err.casefold())):
            return ExitCodes.K8s_EXTN_DELETE_FAILURE.value
        if(self.msg.casefold() == cl_delete_failure_err.casefold()):
            return ExitCodes.CL_DELETE_FAILURE.value
        if(self.msg.casefold() == delete_vCenter_err.casefold()):
            return ExitCodes.VCENTER_DELETE_FAILURE.value
                        
        return exit_code

class InvalidOperation(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.INCORRECT_INPUT.value

class ProgramExit(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class vCenterOperationFailed(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.VCENTER_ENV_FAILURE.value

class InvalidInputError(CustomBaseException):  
    def returnExitCode(self):
        exit_code = ExitCodes.INCORRECT_INPUT.value
        already_onboarded_sddc_err_str = "Cannot Onboard. SDDC is already Arc Onboarded" 

        if(self.msg.casefold() == already_onboarded_sddc_err_str.casefold()):
            return ExitCodes.SDDC_ALREADY_ONBOARDED.value
        
        if(self.msg.__contains__("Invalid config") | self.msg.__contains__("is a required configuration")):
            return ExitCodes.CONFIG_VALIDATION_FAILED.value
        return exit_code

#TODO: (Remove this comment) Should we have a separate error for timeout?
# Should we have a filter here to check for the error msg?
class OperationTimedoutError(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_CREATE_FAILURE.value 

class ArmFeatureNotRegistered(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.FEATURE_NOT_REGISTERED.value

class ClusterExtensionCreationFailed(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.K8s_EXTN_CREATE_FAILURE.value

class ArmProviderNotRegistered(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.RP_NOT_REGISTERED.value

class InvalidRegion(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.INVALID_REGION.value

#TODO: Is this being used?
class InternetNotEnabled(CustomBaseException):  
    def returnExitCode(self):
        return ExitCodes.INTERNET_NOT_ENABLED.value
