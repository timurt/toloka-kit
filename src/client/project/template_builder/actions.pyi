__all__ = [
    'BaseActionV1',
    'BulkActionV1',
    'NotifyActionV1',
    'OpenCloseActionV1',
    'OpenLinkActionV1',
    'PlayPauseActionV1',
    'RotateActionV1',
    'SetActionV1',
    'ToggleActionV1',
]
from toloka.client.project.template_builder.base import (
    BaseComponent,
    BaseTemplate,
    RefComponent
)
from toloka.client.util._extendable_enum import ExtendableStrEnum
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union
)

class BaseActionV1(BaseComponent):
    """Perform various actions, such as showing notifications.
    """

    def __init__(self, *, version: Optional[str] = '1.0.0') -> None:
        """Method generated by attrs for class BaseActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]


class BulkActionV1(BaseActionV1):
    """Use this component to call multiple actions at the same time, like to show more than one notification when a button is clicked.

    Actions are invoked in the order in which they are listed. This means that if two actions write a value to the same
    variable, the variable will always have the second value.
    Attributes:
        payload: An array of actions that you want to call.
    """

    def __init__(
        self,
        payload: Optional[Union[BaseComponent, List[BaseComponent]]] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class BulkActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    payload: Optional[Union[BaseComponent, List[BaseComponent]]]


class NotifyActionV1(BaseActionV1):
    """The component creates a message in the lower-left corner of the screen.

    You can set the how long the message will be active, the delay before displaying it, and the background color.
    Attributes:
        payload: Parameters for the message.
    """

    class Payload(BaseTemplate):
        """Parameters for the message.

        Attributes:
            content: Message text
            theme: The background color of the message.
            delay: The duration of the delay (in milliseconds) before the message appears.
            duration: The duration of the message activity (in milliseconds), which includes the duration of the delay
                before displaying it.
                For example, if duration is 1000 and delay is 400, the message will be displayed for
                600 milliseconds.
        """

        class Theme(ExtendableStrEnum):
            """The background color of the message.

            Attributes:
                INFO: blue
                SUCCESS: green
                WARNING: yellow
                DANGER: red
            """

            DANGER = 'danger'
            INFO = 'info'
            SUCCESS = 'success'
            WARNING = 'warning'

        def __init__(
            self,
            content: Optional[Any] = None,
            theme: Optional[Union[BaseComponent, Theme]] = None,
            *,
            delay: Optional[Union[BaseComponent, float]] = None,
            duration: Optional[Union[BaseComponent, float]] = None
        ) -> None:
            """Method generated by attrs for class NotifyActionV1.Payload.
            """
            ...

        _unexpected: Optional[Dict[str, Any]]
        content: Optional[Any]
        theme: Optional[Union[BaseComponent, Theme]]
        delay: Optional[Union[BaseComponent, float]]
        duration: Optional[Union[BaseComponent, float]]

    def __init__(
        self,
        payload: Optional[Union[BaseComponent, Payload]] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class NotifyActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    payload: Optional[Union[BaseComponent, Payload]]


class OpenCloseActionV1(BaseActionV1):
    """This component changes the display mode of another component by opening or closing it.

    What happens to the component depends on the type of component:
        view.image — expands the image to full screen.
        view.collapse — expands or collapses a collapsible section of content.
    Attributes:
        view: Points to the component to perform the action with.
    """

    def __init__(
        self,
        view: Optional[Union[BaseComponent, RefComponent]] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class OpenCloseActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    view: Optional[Union[BaseComponent, RefComponent]]


class OpenLinkActionV1(BaseActionV1):
    """Opens a new tab in the browser with the specified web page.

    For example, you can open a link when a button is clicked.
    Attributes:
        payload: URL of the web page.
    """

    def __init__(
        self,
        payload: Optional[Any] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class OpenLinkActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    payload: Optional[Any]


class PlayPauseActionV1(BaseActionV1):
    """This component controls audio or video playback. It stops playback in progress or starts if it is stopped.

    For example, this component will allow you to play two videos simultaneously.

    You can also stop or start playback for some event (plugin. trigger) or by pressing the hotkey (plugin.hotkeys).
    Attributes:
        view: Points to the component that plays audio or video.
    """

    def __init__(
        self,
        view: Optional[Union[BaseComponent, RefComponent]] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class PlayPauseActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    view: Optional[Union[BaseComponent, RefComponent]]


class RotateActionV1(BaseActionV1):
    """Rotates the specified component by 90 degrees.

    By default it rotates to the right, but you can specify the direction in the payload property.
    Attributes:
        view: Points to the component to perform the action with.
        payload: Sets the direction of rotation.
    """

    class Payload(ExtendableStrEnum):
        """An enumeration.
        """

        LEFT = 'left'
        RIGHT = 'right'

    def __init__(
        self,
        view: Optional[Union[BaseComponent, RefComponent]] = None,
        payload: Optional[Union[BaseComponent, Payload]] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class RotateActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    view: Optional[Union[BaseComponent, RefComponent]]
    payload: Optional[Union[BaseComponent, Payload]]


class SetActionV1(BaseActionV1):
    """Sets the value from payload in the data in the data property.

    Attributes:
        data: Data with values that will be processed or changed.
        payload: The value to write to the data.
    """

    def __init__(
        self,
        data: Optional[BaseComponent] = None,
        payload: Optional[Any] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class SetActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    data: Optional[BaseComponent]
    payload: Optional[Any]


class ToggleActionV1(BaseActionV1):
    """The component changes the value in the data from true to false and vice versa.

    Attributes:
        data: Data in which the value will be changed. The data type must be boolean.
    """

    def __init__(
        self,
        data: Optional[BaseComponent] = None,
        *,
        version: Optional[str] = '1.0.0'
    ) -> None:
        """Method generated by attrs for class ToggleActionV1.
        """
        ...

    _unexpected: Optional[Dict[str, Any]]
    version: Optional[str]
    data: Optional[BaseComponent]
