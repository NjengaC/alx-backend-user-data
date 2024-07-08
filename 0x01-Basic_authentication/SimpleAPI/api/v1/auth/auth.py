#!/usr/bin/env python3
"""class Auth"""
from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        This method will be used to check if a path requires authentication.
        Currently, it returns False as a placeholder.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        This method will be used to get the Authorization header from the request.
        Currently, it returns None as a placeholder.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        This method will be used to get the current user from the request.
        Currently, it returns None as a placeholder.
        """
        return None
