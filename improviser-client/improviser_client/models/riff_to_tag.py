from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RiffToTag")


@attr.s(auto_attribs=True)
class RiffToTag:
    """ """

    tag_id: str
    riff_id: str
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tag_id = self.tag_id
        riff_id = self.riff_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tag_id": tag_id,
                "riff_id": riff_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_id = d.pop("tag_id")

        riff_id = d.pop("riff_id")

        id = d.pop("id", UNSET)

        riff_to_tag = cls(
            tag_id=tag_id,
            riff_id=riff_id,
            id=id,
        )

        riff_to_tag.additional_properties = d
        return riff_to_tag

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
