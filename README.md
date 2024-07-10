# beezy-ai

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/advanced-setup/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

PIP
```bash
pip install git+<UNSET>.git
```

Poetry
```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Create Chat Completions

This example shows how to create chat completions.

```python
# Synchronous Example
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

if res is not None:
    for event in res:
        # handle event
        print(event)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import beezy_ai
from beezy_ai import BeezyAI
import os

async def main():
    s = BeezyAI(
        api_key_auth=os.getenv("API_KEY_AUTH", ""),
    )
    res = await s.chat.stream_async(request={
        "model": "beezy-small-latest",
        "messages": [
            {
                "role": beezy_ai.ChatCompletionRole.USER,
                "content": "Who is the best French painter? Answer in JSON.",
            },
        ],
        "response_format": {
            "type": "json_object",
        },
        "max_tokens": 512,
        "random_seed": 1337,
    })
    if res is not None:
        for event in res:
            # handle event
            print(event)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [chat](docs/sdks/chat/README.md)

* [stream](docs/sdks/chat/README.md#stream) - Create Chat Completions Stream
* [create](docs/sdks/chat/README.md#create) - Create Chat Completions

### [fim](docs/sdks/fim/README.md)

* [create](docs/sdks/fim/README.md#create) - Create FIM Completions

### [embeddings](docs/sdks/embeddings/README.md)

* [create](docs/sdks/embeddings/README.md#create) - Create Embeddings

### [models](docs/sdks/models/README.md)

* [list](docs/sdks/models/README.md#list) - List Available Models

### [files](docs/sdks/files/README.md)

* [upload](docs/sdks/files/README.md#upload) - Upload File
* [list](docs/sdks/files/README.md#list) - List Files
* [retrieve](docs/sdks/files/README.md#retrieve) - Retrieve File
* [delete](docs/sdks/files/README.md#delete) - Delete File

### [fine_tuning](docs/sdks/finetuning/README.md)

* [list_jobs](docs/sdks/finetuning/README.md#list_jobs) - List Fine Tuning Jobs
* [create_job](docs/sdks/finetuning/README.md#create_job) - Create Fine Tuning Job
* [get_job](docs/sdks/finetuning/README.md#get_job) - Get Fine Tuning Job
* [cancel_job](docs/sdks/finetuning/README.md#cancel_job) - Cancel Fine Tuning Job
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.

```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

if res is not None:
    for event in res:
        # handle event
        print(event)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://wiki.python.org/moin/Generators
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.BadRequest          | 400                        | application/json           |
| models.Unauthorized        | 401                        | application/json           |
| models.Forbidden           | 403                        | application/json           |
| models.NotFound            | 404                        | application/json           |
| models.TooManyRequests     | 429                        | application/json           |
| models.InternalServerError | 500                        | application/json           |
| models.ServiceUnavailable  | 503                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |

### Example

```python
import beezy_ai
from beezy_ai import BeezyAI, models
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)

res = None
try:
    res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

except models.BadRequest as e:
    # handle exception
    raise(e)
except models.Unauthorized as e:
    # handle exception
    raise(e)
except models.Forbidden as e:
    # handle exception
    raise(e)
except models.NotFound as e:
    # handle exception
    raise(e)
except models.TooManyRequests as e:
    # handle exception
    raise(e)
except models.InternalServerError as e:
    # handle exception
    raise(e)
except models.ServiceUnavailable as e:
    # handle exception
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)

if res is not None:
    for event in res:
        # handle event
        print(event)

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Name

You can override the default server globally by passing a server name to the `server: str` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the names associated with the available servers:

| Name | Server | Variables |
| ----- | ------ | --------- |
| `prod` | `https://api.beezy.ai/v1` | None |

#### Example

```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    server="prod",
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

if res is not None:
    for event in res:
        # handle event
        print(event)

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    server_url="https://api.beezy.ai/v1",
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

if res is not None:
    for event in res:
        # handle event
        print(event)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from beezy_ai import BeezyAI
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = BeezyAI(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from beezy_ai import BeezyAI
from beezy_ai.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = BeezyAI(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name           | Type           | Scheme         |
| -------------- | -------------- | -------------- |
| `api_key_auth` | http           | HTTP Bearer    |

To authenticate with the API the `api_key_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.stream(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "Who is the best French painter? Answer in JSON.",
        },
    ],
    "response_format": {
        "type": "json_object",
    },
    "max_tokens": 512,
    "random_seed": 1337,
})

if res is not None:
    for event in res:
        # handle event
        print(event)

```
<!-- End Authentication [security] -->

<!-- Start File uploads [file-upload] -->
## File uploads

Certain SDK methods accept file objects as part of a request body or multi-part request. It is possible and typically recommended to upload files as a stream rather than reading the entire contents into memory. This avoids excessive memory consumption and potentially crashing with out-of-memory errors when working with very large files. The following example demonstrates how to attach a file stream to a request.

> [!TIP]
>
> For endpoints that handle file uploads bytes arrays can also be used. However, using streams is recommended for large files.
>

```python
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.files.upload(purpose="fine-tune", file={
    "file_name": "your_file_here",
    "content": open("<file_path>", "rb"),
})

if res is not None:
    # handle response
    pass

```
<!-- End File uploads [file-upload] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
