# WandbIntegration


## Fields

| Field                                                                           | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `project`                                                                       | *str*                                                                           | :heavy_check_mark:                                                              | The name of the project that the new run will be created under.                 |
| `api_key`                                                                       | *str*                                                                           | :heavy_check_mark:                                                              | The WandB API key to use for authentication.                                    |
| `type`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |
| `name`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | A display name to set for the run. If not set, will use the job ID as the name. |
| `run_name`                                                                      | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | N/A                                                                             |