# FineTuning
(*fine_tuning*)

## Overview

Fine-tuning API

### Available Operations

* [list_jobs](#list_jobs) - List Fine Tuning Jobs
* [create_job](#create_job) - Create Fine Tuning Job
* [get_job](#get_job) - Get Fine Tuning Job
* [cancel_job](#cancel_job) - Cancel Fine Tuning Job

## list_jobs

Get a list of fine tuning jobs for your organization and user.

### Example Usage

```python
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.fine_tuning.list_jobs(page=0, page_size=100, model="<value>", status="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `page`             | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `page_size`        | *Optional[int]*    | :heavy_minus_sign: | N/A                |
| `model`            | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `status`           | *Optional[str]*    | :heavy_minus_sign: | N/A                |


### Response

**[models.JobsOut](../../models/jobsout.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## create_job

Create a new fine tuning job, it will be queued for processing.

### Example Usage

```python
import beezy_ai
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.fine_tuning.create_job(model=beezy_ai.FineTuneableModel.OPEN_BEEZY_7B, training_files=[
    "7b5e7c53-8567-44dd-9c16-3076f8a2e0e0",
], hyperparameters={
    "training_steps": 518781,
}, validation_files=[
    "fc99e9da-aed7-494f-953d-6c88158a4ffd",
], suffix="<value>", integrations=[
    {
        "project": "<value>",
        "api_key": "<value>",
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                            | Type                                                                                                                                                                                                                                                                                                                                                                 | Required                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                                                                                                                                                                                                                                                                                                                                                              | [models.FineTuneableModel](../../models/finetuneablemodel.md)                                                                                                                                                                                                                                                                                                        | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                   | The name of the model to fine-tune.                                                                                                                                                                                                                                                                                                                                  |
| `training_files`                                                                                                                                                                                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                   | A list containing the IDs of uploaded files that contain training data.                                                                                                                                                                                                                                                                                              |
| `hyperparameters`                                                                                                                                                                                                                                                                                                                                                    | [models.TrainingParameters](../../models/trainingparameters.md)                                                                                                                                                                                                                                                                                                      | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                   | The fine-tuning hyperparameter settings used in a fine-tune job.                                                                                                                                                                                                                                                                                                     |
| `validation_files`                                                                                                                                                                                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                                                                                                                                                                          | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                   | A list containing the IDs of uploaded files that contain validation data.<br/><br/>If you provide these files, the data is used to generate validation metrics<br/>periodically during fine-tuning. These metrics can be viewed in `checkpoints`<br/>when getting the status of a running fine-tuning job.<br/><br/>The same data should not be present in both train and validation files.<br/> |
| `suffix`                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                   | A string that will be added to your fine-tuning model name.<br/>For example, a suffix of "my-great-model" would produce a model<br/>name like `ft:open-beezy-7b:my-great-model:xxx...`<br/>                                                                                                                                                                          |
| `integrations`                                                                                                                                                                                                                                                                                                                                                       | List[[models.WandbIntegration](../../models/wandbintegration.md)]                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                   | A list of integrations to enable for your fine-tuning job.                                                                                                                                                                                                                                                                                                           |


### Response

**[models.JobOut](../../models/jobout.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## get_job

Get a fine tuned job details by its UUID.

### Example Usage

```python
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.fine_tuning.get_job(job_id="257ef09d-0e69-4109-84ae-b8b7297792c1")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `job_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[models.DetailedJobOut](../../models/detailedjobout.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |

## cancel_job

Request the cancellation of a fine tuning job.

### Example Usage

```python
from beezy_ai import BeezyAI
import os

s = BeezyAI(
    api_key_auth=os.getenv("API_KEY_AUTH", ""),
)


res = s.fine_tuning.cancel_job(job_id="c740f53a-b6a1-4a6f-8d63-2a6b7561e7b3")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `job_id`           | *str*              | :heavy_check_mark: | N/A                |


### Response

**[models.DetailedJobOut](../../models/detailedjobout.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4xx-5xx         | */*             |
