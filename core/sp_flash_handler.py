#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SP Flash Tool Handler Module
Handles SP Flash Tool operations for MediaTek devices
"""

import logging
import subprocess
from typing import Dict, Optional, Tuple

class SPFlashHandler:
    """Manages SP Flash Tool operations"""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.sp_flash_path = "flash_tool"
    
    def flash_scatter(self, scatter_file: str, comm_port: str = None) -> bool:
        """Flash using scatter file"""
        try:
            cmd = [self.sp_flash_path, "-scatter", scatter_file]
            if comm_port:
                cmd.extend(["-com", comm_port])
            
            result = subprocess.run(cmd, check=True)
            self.logger.info(f"Flash completed with scatter: {scatter_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing with scatter: {e}")
            return False
    
    def read_partition(self, partition: str, output_file: str) -> bool:
        """Read partition from device"""
        try:
            cmd = [
                self.sp_flash_path,
                "-readpart",
                "-part", partition,
                "-output", output_file
            ]
            subprocess.run(cmd, check=True)
            self.logger.info(f"Partition read: {partition} -> {output_file}")
            return True
        except Exception as e:
            self.logger.error(f"Error reading partition: {e}")
            return False
