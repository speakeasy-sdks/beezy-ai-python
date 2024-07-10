# EventOut


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `name`                                                     | *str*                                                      | :heavy_check_mark:                                         | The name of the event.                                     |
| `created_at`                                               | *int*                                                      | :heavy_check_mark:                                         | The UNIX timestamp (in seconds) of the event.              |
| `data`                                                     | [Optional[models.EventOutData]](../models/eventoutdata.md) | :heavy_minus_sign:                                         | The status of the fine-tuning job at the time of the event |