<!-- Start SDK Example Usage [usage] -->
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