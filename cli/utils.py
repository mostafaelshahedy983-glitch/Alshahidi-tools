#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI Utilities Module
Helper functions for CLI
"""

import os
import sys
from typing import Optional

def print_header(text: str):
    """Print formatted header"""
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}\n")

def print_success(message: str):
    """Print success message"""
    print(f"✅ {message}")

def print_error(message: str):
    """Print error message"""
    print(f"❌ {message}", file=sys.stderr)

def print_info(message: str):
    """Print info message"""
    print(f"ℹ️  {message}")
