from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RenderedRiff")


@attr.s(auto_attribs=True)
class RenderedRiff:
    """ """

    render_valid: bool
    image_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        render_valid = self.render_valid
        image_info = self.image_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "render_valid": render_valid,
            }
        )
        if image_info is not UNSET:
            field_dict["image_info"] = image_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        render_valid = d.pop("render_valid")

        image_info = d.pop("image_info", UNSET)

        rendered_riff = cls(
            render_valid=render_valid,
            image_info=image_info,
        )

        rendered_riff.additional_properties = d
        return rendered_riff

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
