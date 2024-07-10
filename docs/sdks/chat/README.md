# Chat
(*chat*)

## Overview

Chat Completion API

### Available Operations

* [stream](#stream) - Create Chat Completions Stream
* [create](#create) - Create Chat Completions

## stream

Create Chat Completions Stream

### Example Usage

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

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `request`                                                                                   | [models.StreamChatCompletionsRequestBody](../../models/streamchatcompletionsrequestbody.md) | :heavy_check_mark:                                                                          | The request object to use for the request.                                                  |


### Response

**[AsyncGenerator[models.ChatCompletionEvent, None]](../../models/.md)**
### Errors

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

## create

Create Chat Completions

### Example Usage

```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.chat.create(request={
    "model": "beezy-small-latest",
    "messages": [
        {
            "role": beezy_ai.ChatCompletionRole.USER,
            "content": "What is the weather like in Paris?",
        },
    ],
    "max_tokens": 64,
    "tools": [
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "Get the current weather in a given location.",
                "parameters": {},
            },
        },
    ],
    "tool_choice": "auto",
    "random_seed": 1337,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.CreateChatCompletionRequestBody](../../models/createchatcompletionrequestbody.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |


### Response

**[models.CreateChatCompletionResponseBody](../../models/createchatcompletionresponsebody.md)**
### Errors

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
