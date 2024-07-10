"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from beezy_ai import models
from beezy_ai._hooks import HookContext
from beezy_ai.types import BaseModel
import beezy_ai.utils as utils
from typing import List, Optional, Union

class FineTuning(BaseSDK):
    r"""Fine-tuning API"""
    
    
    def list_jobs(
        self, *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        model: Optional[str] = None,
        status: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JobsOut:
        r"""List Fine Tuning Jobs

        Get a list of fine tuning jobs for your organization and user.

        :param page: 
        :param page_size: 
        :param model: 
        :param status: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobsRequest(
            page=page,
            page_size=page_size,
            model=model,
            status=status,
        )
        
        req = self.build_request(
            method="GET",
            path="/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_jobs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def list_jobs_async(
        self, *,
        page: Optional[int] = None,
        page_size: Optional[int] = None,
        model: Optional[str] = None,
        status: Optional[str] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JobsOut:
        r"""List Fine Tuning Jobs

        Get a list of fine tuning jobs for your organization and user.

        :param page: 
        :param page_size: 
        :param model: 
        :param status: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobsRequest(
            page=page,
            page_size=page_size,
            model=model,
            status=status,
        )
        
        req = self.build_request(
            method="GET",
            path="/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_jobs", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobsOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def create_job(
        self, *,
        model: models.FineTuneableModel,
        training_files: List[str],
        hyperparameters: Union[models.TrainingParameters, models.TrainingParametersTypedDict],
        validation_files: Optional[List[str]] = None,
        suffix: Optional[str] = None,
        integrations: Optional[Union[List[models.WandbIntegration], List[models.WandbIntegrationTypedDict]]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JobOut:
        r"""Create Fine Tuning Job

        Create a new fine tuning job, it will be queued for processing.

        :param model: The name of the model to fine-tune.
        :param training_files: A list containing the IDs of uploaded files that contain training data.
        :param hyperparameters: The fine-tuning hyperparameter settings used in a fine-tune job.
        :param validation_files: A list containing the IDs of uploaded files that contain validation data.  If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job.  The same data should not be present in both train and validation files.
        :param suffix: A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-beezy-7b:my-great-model:xxx...`
        :param integrations: A list of integrations to enable for your fine-tuning job.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobIn(
            model=model,
            training_files=training_files,
            validation_files=validation_files,
            hyperparameters=utils.unmarshal(hyperparameters, models.TrainingParameters) if not isinstance(hyperparameters, BaseModel) else hyperparameters,
            suffix=suffix,
            integrations=utils.unmarshal(integrations, List[models.WandbIntegration]) if not isinstance(integrations, BaseModel) and integrations is not None else integrations,
        )
        
        req = self.build_request(
            method="POST",
            path="/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.JobIn),
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_create_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def create_job_async(
        self, *,
        model: models.FineTuneableModel,
        training_files: List[str],
        hyperparameters: Union[models.TrainingParameters, models.TrainingParametersTypedDict],
        validation_files: Optional[List[str]] = None,
        suffix: Optional[str] = None,
        integrations: Optional[Union[List[models.WandbIntegration], List[models.WandbIntegrationTypedDict]]] = None,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.JobOut:
        r"""Create Fine Tuning Job

        Create a new fine tuning job, it will be queued for processing.

        :param model: The name of the model to fine-tune.
        :param training_files: A list containing the IDs of uploaded files that contain training data.
        :param hyperparameters: The fine-tuning hyperparameter settings used in a fine-tune job.
        :param validation_files: A list containing the IDs of uploaded files that contain validation data.  If you provide these files, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in `checkpoints` when getting the status of a running fine-tuning job.  The same data should not be present in both train and validation files.
        :param suffix: A string that will be added to your fine-tuning model name. For example, a suffix of \"my-great-model\" would produce a model name like `ft:open-beezy-7b:my-great-model:xxx...`
        :param integrations: A list of integrations to enable for your fine-tuning job.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobIn(
            model=model,
            training_files=training_files,
            validation_files=validation_files,
            hyperparameters=utils.unmarshal(hyperparameters, models.TrainingParameters) if not isinstance(hyperparameters, BaseModel) else hyperparameters,
            suffix=suffix,
            integrations=utils.unmarshal(integrations, List[models.WandbIntegration]) if not isinstance(integrations, BaseModel) and integrations is not None else integrations,
        )
        
        req = self.build_request(
            method="POST",
            path="/fine_tuning/jobs",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", models.JobIn),
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_create_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.JobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def get_job(
        self, *,
        job_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DetailedJobOut:
        r"""Get Fine Tuning Job

        Get a fine tuned job details by its UUID.

        :param job_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/fine_tuning/jobs/{job_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def get_job_async(
        self, *,
        job_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DetailedJobOut:
        r"""Get Fine Tuning Job

        Get a fine tuned job details by its UUID.

        :param job_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningGetFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/fine_tuning/jobs/{job_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_get_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def cancel_job(
        self, *,
        job_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DetailedJobOut:
        r"""Cancel Fine Tuning Job

        Request the cancellation of a fine tuning job.

        :param job_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningCancelFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/fine_tuning/jobs/{job_id}/cancel",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_cancel_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def cancel_job_async(
        self, *,
        job_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DetailedJobOut:
        r"""Cancel Fine Tuning Job

        Request the cancellation of a fine tuning job.

        :param job_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.JobsAPIRoutesFineTuningCancelFineTuningJobRequest(
            job_id=job_id,
        )
        
        req = self.build_request(
            method="POST",
            path="/fine_tuning/jobs/{job_id}/cancel",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="jobs_api_routes_fine_tuning_cancel_fine_tuning_job", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DetailedJobOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    