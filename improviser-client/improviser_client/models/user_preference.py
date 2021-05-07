from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreference")


@attr.s(auto_attribs=True)
class UserPreference:
    """ """

    instrument_id: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instrument_id = self.instrument_id
        language = self.language

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instrument_id is not UNSET:
            field_dict["instrument_id"] = instrument_id
        if language is not UNSET:
            field_dict["language"] = language

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instrument_id = d.pop("instrument_id", UNSET)

        language = d.pop("language", UNSET)

        user_preference = cls(
            instrument_id=instrument_id,
            language=language,
        )

        user_preference.additional_properties = d
        return user_preference

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
