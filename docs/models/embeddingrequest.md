# EmbeddingRequest


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `model`                                                        | *Optional[str]*                                                | :heavy_minus_sign:                                             | The ID of the model to use for this request.<br/>              | beezy-embed                                                    |
| `inputs`                                                       | List[*str*]                                                    | :heavy_minus_sign:                                             | The list of strings to embed.<br/>                             | [<br/>"Hello",<br/>"world"<br/>]                               |
| `encoding_format`                                              | [Optional[models.EncodingFormat]](../models/encodingformat.md) | :heavy_minus_sign:                                             | The format of the output data.<br/>                            | float                                                          |