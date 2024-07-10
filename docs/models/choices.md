# Choices


## Fields

| Field                                                                                                  | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `index`                                                                                                | *int*                                                                                                  | :heavy_check_mark:                                                                                     | N/A                                                                                                    | 0                                                                                                      |
| `finish_reason`                                                                                        | [Nullable[models.ChatCompletionResponseFinishReason]](../models/chatcompletionresponsefinishreason.md) | :heavy_check_mark:                                                                                     | N/A                                                                                                    | stop                                                                                                   |
| `message`                                                                                              | [Optional[models.Message]](../models/message.md)                                                       | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |