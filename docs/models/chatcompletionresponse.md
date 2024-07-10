# ChatCompletionResponse


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  | Example                                      |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `id`                                         | *Optional[str]*                              | :heavy_minus_sign:                           | N/A                                          | cmpl-e5cc70bb28c444948073e77776eb30ef        |
| `object`                                     | *Optional[str]*                              | :heavy_minus_sign:                           | N/A                                          | chat.completion                              |
| `created`                                    | *Optional[int]*                              | :heavy_minus_sign:                           | N/A                                          | 1702256327                                   |
| `model`                                      | *Optional[str]*                              | :heavy_minus_sign:                           | N/A                                          | beezy-small-latest                           |
| `choices`                                    | List[[models.Choices](../models/choices.md)] | :heavy_minus_sign:                           | N/A                                          |                                              |
| `usage`                                      | [Optional[models.Usage]](../models/usage.md) | :heavy_minus_sign:                           | N/A                                          |                                              |