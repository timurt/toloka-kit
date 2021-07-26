__all__ = [
    'SpecClassIdentificationError',
    'ApiError',
    'ValidationApiError',
    'InternalApiError',
    'AuthenticationApiError',
    'AccessDeniedApiError',
    'RemoteServiceUnavailableApiError',
    'DoesNotExistApiError',
    'ConflictStateApiError',
    'TooManyRequestsApiError',
    'IncorrectActionsApiError',
    'raise_on_api_error',
]
from requests.models import Response
from typing import (
    Any,
    List,
    Optional
)

class SpecClassIdentificationError(Exception):
    """Raised when cannot find spec_сlass for spec_field value.

    Attributes:
        spec_field: value that defines spec_class type
        spec_enum: enum class containing spec_class possible types
    """

    def __init__(
        self,
        *,
        spec_field: Optional[str] = None,
        spec_enum: Optional[str] = None
    ) -> None:
        """Method generated by attrs for class SpecClassIdentificationError.
        """
        ...

    spec_field: Optional[str]
    spec_enum: Optional[str]


class ApiError(Exception):
    """Error returned from the API Call.

    Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    def __init__(
        self,
        *,
        status_code: Optional[int] = None,
        request_id: Optional[str] = None,
        code: Optional[str] = None,
        message: Optional[str] = None,
        payload: Optional[Any] = None
    ) -> None:
        """Method generated by attrs for class ApiError.
        """
        ...

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class ValidationApiError(ApiError):
    """Field validation error returned from the API Call.

    Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
        invalid_fields: the list of the invalid fields
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]
    _invalid_fields: Optional[List[str]]


class InternalApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class AuthenticationApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class AccessDeniedApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class RemoteServiceUnavailableApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class DoesNotExistApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class ConflictStateApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class TooManyRequestsApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


class IncorrectActionsApiError(ApiError):
    """Attributes:
        status_code: response status code.
        request_id: request ID
        code: error code string
        message: error message
        payload: additional payload
    """

    status_code: Optional[int]
    request_id: Optional[str]
    code: Optional[str]
    message: Optional[str]
    payload: Optional[Any]


def raise_on_api_error(response: Response): ...
