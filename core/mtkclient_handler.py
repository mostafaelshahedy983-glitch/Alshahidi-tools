#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MTKClient Handler Module
Handles MediaTek device operations via MTKClient
"""

import logging
import subprocess
from typing import Dict, Optional, Tuple

class MTKClientHandler:
    """Manages MTKClient operations for MediaTek devices"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.mtkclient_path = "mtkclient"
    
    def flash_rom(self, rom_path: str, device_port: str = None) -> bool:
        """Flash ROM using MTKClient"""
        try:
            cmd = [self.mtkclient_path, "--flash", rom_path]
            if device_port:
                cmd.extend(["--port", device_port])
            
            result = subprocess.run(cmd, check=True)
            self.logger.info(f"ROM flashed successfully: {rom_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing ROM with MTKClient: {e}")
            return False
    
    def read_memory(self, address: str, length: str, output_file: str) -> bool:
        """Read device memory"""
        try:
            cmd = [
                self.mtkclient_path,
                "--read",
                "--address", address,
                "--length", length,
                "--output", output_file
            ]
            subprocess.run(cmd, check=True)
            self.logger.info(f"Memory read: {address} (length: {length})")
            return True
        except Exception as e:
            self.logger.error(f"Error reading memory: {e}")
            return False
    
    def write_memory(self, address: str, data_file: str) -> bool:
        """Write to device memory"""
        try:
            cmd = [
                self.mtkclient_path,
                "--write",
                "--address", address,
                "--input", data_file
            ]
            subprocess.run(cmd, check=True)
            self.logger.info(f"Memory written: {address}")
            return True
        except Exception as e:
            self.logger.error(f"Error writing memory: {e}")
            return False
    
    def get_device_info(self) -> Dict[str, str]:
        """Get MediaTek device information"""
        try:
            result = subprocess.run(
                [self.mtkclient_path, "--info"],
                capture_output=True,
                text=True
            )
            info = {}
            for line in result.stdout.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    info[key.strip()] = value.strip()
            return info
        except Exception as e:
            self.logger.error(f"Error getting device info: {e}")
            return {}
