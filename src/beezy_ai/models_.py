"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from beezy_ai import models
from beezy_ai._hooks import HookContext
import beezy_ai.utils as utils
from typing import Optional

class Models(BaseSDK):
    r"""Model Management API"""
    
    
    def list(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ModelList:
        r"""List Available Models

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/models",
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
            hook_ctx=HookContext(operation_id="listModels", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelList])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    
    
    async def list_async(
        self, *,
        server_url: Optional[str] = None,
        timeout_config: Optional[int] = None,
    ) -> models.ModelList:
        r"""List Available Models

        :param server_url: Override the default server URL for this method
        :param timeout_config: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        req = self.build_request(
            method="GET",
            path="/models",
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
            hook_ctx=HookContext(operation_id="listModels", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["4XX","5XX"],
        )
        
        
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.ModelList])
        if utils.match_response(http_res, ["4XX","5XX"], "*"):
            raise models.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        
        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(f"Unexpected response received (code: {http_res.status_code}, type: {content_type})", http_res.status_code, http_res.text, http_res)
    