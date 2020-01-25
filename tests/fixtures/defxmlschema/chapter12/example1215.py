from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class ProductType:
    """
    :ivar number:
    :ivar name:
    :ivar size:
    :ivar color:
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            namespace="",
            required=True
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            namespace="",
            required=True
        )
    )
    size: Optional[Union[int, str]] = field(
        default=None,
        metadata=dict(
            name="size",
            type="Element",
            namespace="",
            min_inclusive=2.0,
            max_inclusive=18.0
        )
    )
    color: Optional[str] = field(
        default=None,
        metadata=dict(
            name="color",
            type="Element",
            namespace=""
        )
    )