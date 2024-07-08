#!/usr/bin/env python3
"""class Auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if the path requires authentication.
        """
        if path is None:
            return True
        
        if not excluded_paths or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'
        
        for ex_path in excluded_paths:
            if ex_path[-1] != '/':
                ex_path += '/'
            if path == ex_path:
                return False

        return True


    def authorization_header(self, request=None) -> str:
        """
        Get the Authorization header from the request.
        """
        if request is None:
            return None
        
        auth_header = request.headers.get('Authorization')
        if auth_header is None:
            return None
        
        return auth_header


    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method will be used to get the current user from the request.
        Currently, it returns None as a placeholder.
        """
        return None
