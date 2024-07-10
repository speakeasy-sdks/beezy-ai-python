# Embeddings
(*embeddings*)

## Overview

Embeddings API

### Available Operations

* [create](#create) - Create Embeddings

## create

Create Embeddings

### Example Usage

```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.embeddings.create(model="beezy-embed", inputs=[
    "Hello",
    "world",
], encoding_format=beezy_ai.EncodingFormat.FLOAT)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                         | Type                                                              | Required                                                          | Description                                                       | Example                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `model`                                                           | *Optional[str]*                                                   | :heavy_minus_sign:                                                | The ID of the model to use for this request.<br/>                 | beezy-embed                                                       |
| `inputs`                                                          | List[*str*]                                                       | :heavy_minus_sign:                                                | The list of strings to embed.<br/>                                | [<br/>"Hello",<br/>"world"<br/>]                                  |
| `encoding_format`                                                 | [Optional[models.EncodingFormat]](../../models/encodingformat.md) | :heavy_minus_sign:                                                | The format of the output data.<br/>                               | float                                                             |


### Response

**[models.EmbeddingResponse](../../models/embeddingresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
