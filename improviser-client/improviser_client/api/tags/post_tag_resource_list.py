from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.tag import Tag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: Tag,
    x_fields: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/tags/".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if x_fields is not UNSET:
        headers["x-fields"] = x_fields

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Tag]:
    if response.status_code == 200:
        response_200 = Tag.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Tag]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Tag,
    x_fields: Union[Unset, str] = UNSET,
) -> Response[Tag]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_fields=x_fields,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: Tag,
    x_fields: Union[Unset, str] = UNSET,
) -> Optional[Tag]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_fields=x_fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Tag,
    x_fields: Union[Unset, str] = UNSET,
) -> Response[Tag]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        x_fields=x_fields,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: Tag,
    x_fields: Union[Unset, str] = UNSET,
) -> Optional[Tag]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_fields=x_fields,
        )
    ).parsed
