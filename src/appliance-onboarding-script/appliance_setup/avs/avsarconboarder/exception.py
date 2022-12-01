from common_exceptions import CustomBaseException, ExitCodes

class InvalidDataException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class ValidationFailedException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class UnexpectedRetrievalException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class VCSADetailsNotFoundException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR.value

class InternetEnabledFlagNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.INTERNET_NOT_ENABLED.value

class ManagementClusterNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR.value

class UnexpectedCreatorException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class VNETIPCIDRNotFound(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR.value

class InvalidInputError(CustomBaseException):
    def returnExitCode(self):
        exit_code = ExitCodes.INCORRECT_INPUT.value
        already_onboarded_sddc_err_str = "Cannot Onboard. SDDC is already Arc Onboarded" 

        if(self.msg.casefold() == already_onboarded_sddc_err_str.casefold()):
            return ExitCodes.SDDC_ALREADY_ONBOARDED.value
        
        if(self.msg.__contains__("Invalid config") | self.msg.__contains__("is a required configuration")):
            return ExitCodes.CONFIG_VALIDATION_FAILED.value
        return exit_code

class DataNotFoundException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.FETCH_SDDC_DETAILS_ERROR.value

class AlreadyExistsException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class CreationException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class DHCPCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class DNSZoneCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class DNSServerCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class SegmentCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class ArcAddOnCreationException(CreationException):
    def returnExitCode(self):
        return ExitCodes.VCENTER_REGISTER_FAILURE.value

class DeletionException(CustomBaseException):
    def returnExitCode(self):
        return ExitCodes.GENERIC_ERROR.value

class ArcAddOnDeletionException(DeletionException):
    def returnExitCode(self):
        return ExitCodes.VCENTER_DEREGISTER_FAILURE.value
