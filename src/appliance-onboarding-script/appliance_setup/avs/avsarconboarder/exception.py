from common_exceptions import CustomBaseException, ExitCodes

class InvalidDataException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class ValidationFailedException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class UnexpectedRetrievalException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class VCSADetailsNotFoundException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR

class InternetEnabledFlagNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.INTERNET_NOT_ENABLED

class ManagementClusterNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR

class UnexpectedCreatorException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class VNETIPCIDRNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR

class InvalidInputError(CustomBaseException):
    def returnExitCode(self):
        exit_code = ExitCodes.INCORRECT_INPUT
        already_onboarded_sddc_err_str = "Cannot Onboard. SDDC is already Arc Onboarded" 

        if(self.msg.casefold() == already_onboarded_sddc_err_str.casefold):
            return ExitCodes.SDDC_ALREADY_ONBOARDED
        
        if(self.msg.contains("Invalid config") | self.msg.contains("is a required configuration")):
            return ExitCodes.CONFIG_VALIDATION_FAILED
        return exit_code

class DataNotFoundException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR

class AlreadyExistsException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class CreationException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class DHCPCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class DNSZoneCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class DNSServerCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class SegmentCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class ArcAddOnCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.VCENTER_REGISTER_FAILURE

class DeletionException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR

class ArcAddOnDeletionException(DeletionException):
    def returnExitCode(self):
        return ExitCodes.VCENTER_DEREGISTER_FAILURE
