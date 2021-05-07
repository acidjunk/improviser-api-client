from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    search_phrase: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/exercises/scales".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "search_phrase": search_phrase,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    search_phrase: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        search_phrase=search_phrase,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    search_phrase: Union[Unset, str] = UNSET,
) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
        search_phrase=search_phrase,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
