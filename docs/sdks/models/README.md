# Models
(*models*)

## Overview

Model Management API

### Available Operations

* [list](#list) - List Available Models

## list

List Available Models

### Example Usage

```python
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.models.list()

if res is not None:
    # handle response
    pass

```


### Response

**[models.ModelList](../../models/modellist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
