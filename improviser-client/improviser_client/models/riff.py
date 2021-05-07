from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Riff")


@attr.s(auto_attribs=True)
class Riff:
    """ """

    name: str
    number_of_bars: int
    notes: str
    id: Union[Unset, str] = UNSET
    chord: Union[Unset, str] = UNSET
    multi_chord: Union[Unset, bool] = UNSET
    scale_trainer_enabled: Union[Unset, bool] = UNSET
    chord_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        number_of_bars = self.number_of_bars
        notes = self.notes
        id = self.id
        chord = self.chord
        multi_chord = self.multi_chord
        scale_trainer_enabled = self.scale_trainer_enabled
        chord_info = self.chord_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "number_of_bars": number_of_bars,
                "notes": notes,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if chord is not UNSET:
            field_dict["chord"] = chord
        if multi_chord is not UNSET:
            field_dict["multi_chord"] = multi_chord
        if scale_trainer_enabled is not UNSET:
            field_dict["scale_trainer_enabled"] = scale_trainer_enabled
        if chord_info is not UNSET:
            field_dict["chord_info"] = chord_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        number_of_bars = d.pop("number_of_bars")

        notes = d.pop("notes")

        id = d.pop("id", UNSET)

        chord = d.pop("chord", UNSET)

        multi_chord = d.pop("multi_chord", UNSET)

        scale_trainer_enabled = d.pop("scale_trainer_enabled", UNSET)

        chord_info = d.pop("chord_info", UNSET)

        riff = cls(
            name=name,
            number_of_bars=number_of_bars,
            notes=notes,
            id=id,
            chord=chord,
            multi_chord=multi_chord,
            scale_trainer_enabled=scale_trainer_enabled,
            chord_info=chord_info,
        )

        riff.additional_properties = d
        return riff

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
