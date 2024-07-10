# ChatCompletionResponseFunctionCallChoices


## Fields

| Field                                                                                                                          | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    | Example                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `index`                                                                                                                        | *int*                                                                                                                          | :heavy_check_mark:                                                                                                             | N/A                                                                                                                            | 0                                                                                                                              |
| `finish_reason`                                                                                                                | [Nullable[models.ChatCompletionResponseFunctionCallFinishReason]](../models/chatcompletionresponsefunctioncallfinishreason.md) | :heavy_check_mark:                                                                                                             | N/A                                                                                                                            | tool_calls                                                                                                                     |
| `message`                                                                                                                      | [Optional[models.ChatCompletionResponseFunctionCallMessage]](../models/chatcompletionresponsefunctioncallmessage.md)           | :heavy_minus_sign:                                                                                                             | N/A                                                                                                                            |                                                                                                                                |