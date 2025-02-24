__all__ = [
    'actions',
    'base',
    'conditions',
    'data',
    'fields',
    'helpers',
    'layouts',
    'plugins',
    'view',
    'TemplateBuilder',
    'get_input_and_output',
    'BulkActionV1',
    'NotifyActionV1',
    'OpenCloseActionV1',
    'OpenLinkActionV1',
    'PlayPauseActionV1',
    'RotateActionV1',
    'SetActionV1',
    'ToggleActionV1',
    'AllConditionV1',
    'AnyConditionV1',
    'DistanceConditionV1',
    'EmptyConditionV1',
    'EqualsConditionV1',
    'LinkOpenedConditionV1',
    'NotConditionV1',
    'PlayedConditionV1',
    'PlayedFullyConditionV1',
    'RequiredConditionV1',
    'SameDomainConditionV1',
    'SchemaConditionV1',
    'SubArrayConditionV1',
    'InputData',
    'InternalData',
    'LocalData',
    'LocationData',
    'OutputData',
    'RelativeData',
    'AudioFieldV1',
    'ButtonRadioFieldV1',
    'GroupFieldOption',
    'ButtonRadioGroupFieldV1',
    'CheckboxFieldV1',
    'CheckboxGroupFieldV1',
    'DateFieldV1',
    'EmailFieldV1',
    'FileFieldV1',
    'ImageAnnotationFieldV1',
    'ListFieldV1',
    'MediaFileFieldV1',
    'NumberFieldV1',
    'PhoneNumberFieldV1',
    'RadioGroupFieldV1',
    'SelectFieldV1',
    'TextFieldV1',
    'TextAnnotationFieldV1',
    'TextareaFieldV1',
    'ConcatArraysHelperV1',
    'Entries2ObjectHelperV1',
    'IfHelperV1',
    'JoinHelperV1',
    'Object2EntriesHelperV1',
    'ReplaceHelperV1',
    'SearchQueryHelperV1',
    'SwitchHelperV1',
    'TextTransformHelperV1',
    'TransformHelperV1',
    'TranslateHelperV1',
    'YandexDiskProxyHelperV1',
    'BarsLayoutV1',
    'ColumnsLayoutV1',
    'CompareLayoutItem',
    'CompareLayoutV1',
    'SideBySideLayoutV1',
    'SidebarLayoutV1',
    'ImageAnnotationHotkeysPluginV1',
    'TextAnnotationHotkeysPluginV1',
    'HotkeysPluginV1',
    'TriggerPluginV1',
    'TolokaPluginV1',
    'ActionButtonViewV1',
    'AlertViewV1',
    'AudioViewV1',
    'CollapseViewV1',
    'DeviceFrameViewV1',
    'DividerViewV1',
    'GroupViewV1',
    'IframeViewV1',
    'ImageViewV1',
    'LabeledListViewV1',
    'LinkViewV1',
    'LinkGroupViewV1',
    'ListViewV1',
    'MarkdownViewV1',
    'TextViewV1',
    'VideoViewV1',
]
import toloka.client.primitives.base
import toloka.client.project.field_spec
import toloka.client.project.template_builder.base
import typing

from toloka.client.project.template_builder import (
    actions,
    base,
    conditions,
    data,
    fields,
    helpers,
    layouts,
    plugins,
    view
)
from toloka.client.project.template_builder.actions import (
    BulkActionV1,
    NotifyActionV1,
    OpenCloseActionV1,
    OpenLinkActionV1,
    PlayPauseActionV1,
    RotateActionV1,
    SetActionV1,
    ToggleActionV1
)
from toloka.client.project.template_builder.conditions import (
    AllConditionV1,
    AnyConditionV1,
    DistanceConditionV1,
    EmptyConditionV1,
    EqualsConditionV1,
    LinkOpenedConditionV1,
    NotConditionV1,
    PlayedConditionV1,
    PlayedFullyConditionV1,
    RequiredConditionV1,
    SameDomainConditionV1,
    SchemaConditionV1,
    SubArrayConditionV1
)
from toloka.client.project.template_builder.data import (
    InputData,
    InternalData,
    LocalData,
    LocationData,
    OutputData,
    RelativeData
)
from toloka.client.project.template_builder.fields import (
    AudioFieldV1,
    ButtonRadioFieldV1,
    ButtonRadioGroupFieldV1,
    CheckboxFieldV1,
    CheckboxGroupFieldV1,
    DateFieldV1,
    EmailFieldV1,
    FileFieldV1,
    GroupFieldOption,
    ImageAnnotationFieldV1,
    ListFieldV1,
    MediaFileFieldV1,
    NumberFieldV1,
    PhoneNumberFieldV1,
    RadioGroupFieldV1,
    SelectFieldV1,
    TextAnnotationFieldV1,
    TextFieldV1,
    TextareaFieldV1
)
from toloka.client.project.template_builder.helpers import (
    ConcatArraysHelperV1,
    Entries2ObjectHelperV1,
    IfHelperV1,
    JoinHelperV1,
    Object2EntriesHelperV1,
    ReplaceHelperV1,
    SearchQueryHelperV1,
    SwitchHelperV1,
    TextTransformHelperV1,
    TransformHelperV1,
    TranslateHelperV1,
    YandexDiskProxyHelperV1
)
from toloka.client.project.template_builder.layouts import (
    BarsLayoutV1,
    ColumnsLayoutV1,
    CompareLayoutItem,
    CompareLayoutV1,
    SideBySideLayoutV1,
    SidebarLayoutV1
)
from toloka.client.project.template_builder.plugins import (
    HotkeysPluginV1,
    ImageAnnotationHotkeysPluginV1,
    TextAnnotationHotkeysPluginV1,
    TolokaPluginV1,
    TriggerPluginV1
)
from toloka.client.project.template_builder.view import (
    ActionButtonViewV1,
    AlertViewV1,
    AudioViewV1,
    CollapseViewV1,
    DeviceFrameViewV1,
    DividerViewV1,
    GroupViewV1,
    IframeViewV1,
    ImageViewV1,
    LabeledListViewV1,
    LinkGroupViewV1,
    LinkViewV1,
    ListViewV1,
    MarkdownViewV1,
    TextViewV1,
    VideoViewV1
)

class TemplateBuilder(toloka.client.primitives.base.BaseTolokaObject):
    def __init__(
        self,
        *,
        view: typing.Optional[toloka.client.project.template_builder.base.BaseComponent] = None,
        plugins: typing.Optional[typing.List[toloka.client.project.template_builder.base.BaseComponent]] = None,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = None
    ) -> None:
        """Method generated by attrs for class TemplateBuilder.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    view: typing.Optional[toloka.client.project.template_builder.base.BaseComponent]
    plugins: typing.Optional[typing.List[toloka.client.project.template_builder.base.BaseComponent]]
    vars: typing.Optional[typing.Dict[str, typing.Any]]


def get_input_and_output(tb_config: typing.Union[dict, TemplateBuilder]) -> typing.Tuple[typing.Dict[str, toloka.client.project.field_spec.FieldSpec], typing.Dict[str, toloka.client.project.field_spec.FieldSpec]]: ...
