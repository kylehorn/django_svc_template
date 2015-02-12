from rest_framework.views import exception_handler
from . import constants


def application_exception_handler(exception):
    response = exception_handler(exception)

    if response:
        response.data[
            constants.API_ERROR_STATUS_CODE_KEY] = response.status_code
        response.data[
            constants.API_ERROR_MESSAGE_KEY] = response.data.pop('detail')
        error = response.data
        response.data = {}
        response.data[constants.API_ERROR_KEY] = error

    return response
