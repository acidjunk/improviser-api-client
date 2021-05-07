from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RecentExercise")


@attr.s(auto_attribs=True)
class RecentExercise:
    """ """

    riff_exercise_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        riff_exercise_id = self.riff_exercise_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "riff_exercise_id": riff_exercise_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        riff_exercise_id = d.pop("riff_exercise_id")

        recent_exercise = cls(
            riff_exercise_id=riff_exercise_id,
        )

        recent_exercise.additional_properties = d
        return recent_exercise

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
