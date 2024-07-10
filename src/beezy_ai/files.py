"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from beezy_ai import models
from beezy_ai._hooks import HookContext
from beezy_ai.types import BaseModel
import beezy_ai.utils as utils
from typing import Optional, Union

class Files(BaseSDK):
    r"""Files API"""
    
    
    def upload(
        self, *,
        purpose: str,
        file: Union[models.File, models.FileTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.UploadFileOut:
        r"""Upload File

        Upload a file that can be used across various endpoints.

        The size of individual files can be a maximum of 512 MB. The Fine-tuning API only supports .jsonl files.

        Please contact us if you need to increase these storage limits.

        :param purpose: The intended purpose of the uploaded file. Only accepts fine-tuning (`fine-tune`) for now.
        :param file: The File object (not file name) to be uploaded.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.UploadFile(
            purpose=purpose,
            file=utils.unmarshal(file, models.File) if not isinstance(file, BaseModel) else file,
        )
        
        req = self.build_request(
            method="POST",
            path="/files",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "multipart", models.UploadFile),
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="files_api_routes_upload_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.UploadFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def upload_async(
        self, *,
        purpose: str,
        file: Union[models.File, models.FileTypedDict],
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.UploadFileOut:
        r"""Upload File

        Upload a file that can be used across various endpoints.

        The size of individual files can be a maximum of 512 MB. The Fine-tuning API only supports .jsonl files.

        Please contact us if you need to increase these storage limits.

        :param purpose: The intended purpose of the uploaded file. Only accepts fine-tuning (`fine-tune`) for now.
        :param file: The File object (not file name) to be uploaded.
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.UploadFile(
            purpose=purpose,
            file=utils.unmarshal(file, models.File) if not isinstance(file, BaseModel) else file,
        )
        
        req = self.build_request(
            method="POST",
            path="/files",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "multipart", models.UploadFile),
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="files_api_routes_upload_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.UploadFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def list(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ListFilesOut:
        r"""List Files

        Returns a list of files that belong to the user's organization.

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/files",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="files_api_routes_list_files", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ListFilesOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def list_async(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ListFilesOut:
        r"""List Files

        Returns a list of files that belong to the user's organization.

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/files",
            base_url=base_url,
            url_variables=url_variables,
            request=None,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_config=timeout_config,
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="files_api_routes_list_files", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ListFilesOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def retrieve(
        self, *,
        file_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.RetrieveFileOut:
        r"""Retrieve File

        Returns information about a specific file.

        :param file_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.FilesAPIRoutesRetrieveFileRequest(
            file_id=file_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/files/{file_id}",
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
            hook_ctx=HookContext(operation_id="files_api_routes_retrieve_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.RetrieveFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def retrieve_async(
        self, *,
        file_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.RetrieveFileOut:
        r"""Retrieve File

        Returns information about a specific file.

        :param file_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.FilesAPIRoutesRetrieveFileRequest(
            file_id=file_id,
        )
        
        req = self.build_request(
            method="GET",
            path="/files/{file_id}",
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
            hook_ctx=HookContext(operation_id="files_api_routes_retrieve_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.RetrieveFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    def delete(
        self, *,
        file_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeleteFileOut:
        r"""Delete File

        Delete a file.

        :param file_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.FilesAPIRoutesDeleteFileRequest(
            file_id=file_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/files/{file_id}",
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
            hook_ctx=HookContext(operation_id="files_api_routes_delete_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeleteFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def delete_async(
        self, *,
        file_id: str,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.DeleteFileOut:
        r"""Delete File

        Delete a file.

        :param file_id: 
        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = models.FilesAPIRoutesDeleteFileRequest(
            file_id=file_id,
        )
        
        req = self.build_request(
            method="DELETE",
            path="/files/{file_id}",
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
            hook_ctx=HookContext(operation_id="files_api_routes_delete_file", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.DeleteFileOut])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
