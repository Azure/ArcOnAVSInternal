#!/usr/bin/python

# These are the exceptions used across different modules.
from common_exceptions import CustomBaseException, ExitCodes

class FilePathNotFoundInArgs(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.CONFIG_NOT_FOUND.value

class AzCommandError(CustomBaseException): 
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value
        
class AzArcApplianceValidateError(AzCommandError) :
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_VALIDATE_FAILURE.value

class AzArcAppliancePrepareError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_PREPARE_FAILURE.value

class AzArcApplianceDeployError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_DEPLOY_FAILURE.value

class AzArcApplianceCreateError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_CREATE_FAILURE.value

class AzArcApplianceDeleteError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.ARC_APPLIANCE_DELETE_FAILURE.value

class K8sExtnCreateError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.K8s_EXTN_CREATE_FAILURE.value

class K8sExtnDeleteError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.K8s_EXTN_DELETE_FAILURE.value

class CLCreateError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.CL_CREATE_FAILURE.value  

class CLDeleteError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.CL_DELETE_FAILURE.value  

class VCenterCreatError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.VCENTER_CREATE_FAILURE.value

class VCenterDeleteError(AzCommandError):
    def returnExitCode(self):
        return ExitCodes.VCENTER_DELETE_FAILURE.value

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
        return ExitCodes.INCORRECT_INPUT.value

class SDDCOnboardedError(InvalidInputError):
    def returnExitCode(self):
        return ExitCodes.SDDC_ALREADY_ONBOARDED.value

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
