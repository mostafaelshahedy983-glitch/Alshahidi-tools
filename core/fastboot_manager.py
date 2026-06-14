#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fastboot Manager Module
Handles fastboot operations for bootloader access
"""

import subprocess
import logging
from typing import List, Dict, Optional, Tuple
import time

class FastbootManager:
    """Manages Fastboot operations"""
    
    def __init__(self, fastboot_path: str = "fastboot"):
        self.fastboot_path = fastboot_path
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def get_devices(self) -> List[str]:
        """Get list of devices in fastboot mode"""
        try:
            result = subprocess.run(
                [self.fastboot_path, "devices"],
                capture_output=True,
                text=True
            )
            devices = []
            for line in result.stdout.split('\n'):
                if line.strip() and not line.startswith("List"):
                    device_id = line.split()[0]
                    if device_id:
                        devices.append(device_id)
            return devices
        except Exception as e:
            self.logger.error(f"Error getting fastboot devices: {e}")
            return []
    
    def flash_partition(self, device_id: str, partition: str, image_path: str) -> bool:
        """Flash a partition with image"""
        try:
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "flash", partition, image_path],
                check=True
            )
            self.logger.info(f"Partition flashed: {partition} <- {image_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing partition: {e}")
            return False
    
    def flash_rom(self, device_id: str, rom_path: str) -> bool:
        """Flash complete ROM"""
        try:
            self.logger.info(f"Starting ROM flash: {rom_path}")
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "flash", "system", rom_path],
                check=True
            )
            self.logger.info("ROM flashed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing ROM: {e}")
            return False
    
    def flash_recovery(self, device_id: str, recovery_path: str) -> bool:
        """Flash custom recovery"""
        try:
            self.logger.info(f"Flashing recovery: {recovery_path}")
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "flash", "recovery", recovery_path],
                check=True
            )
            self.logger.info("Recovery flashed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing recovery: {e}")
            return False
    
    def flash_bootloader(self, device_id: str, bootloader_path: str) -> bool:
        """Flash bootloader"""
        try:
            self.logger.info(f"Flashing bootloader: {bootloader_path}")
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "flash", "bootloader", bootloader_path],
                check=True
            )
            self.logger.info("Bootloader flashed successfully")
            return True
        except Exception as e:
            self.logger.error(f"Error flashing bootloader: {e}")
            return False
    
    def erase_partition(self, device_id: str, partition: str) -> bool:
        """Erase a partition"""
        try:
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "erase", partition],
                check=True
            )
            self.logger.info(f"Partition erased: {partition}")
            return True
        except Exception as e:
            self.logger.error(f"Error erasing partition: {e}")
            return False
    
    def reboot(self, device_id: str) -> bool:
        """Reboot device from fastboot"""
        try:
            subprocess.run(
                [self.fastboot_path, "-s", device_id, "reboot"],
                check=True
            )
            self.logger.info("Device rebooted")
            return True
        except Exception as e:
            self.logger.error(f"Error rebooting: {e}")
            return False
    
    def get_info(self, device_id: str, variable: str) -> Optional[str]:
        """Get device info variable"""
        try:
            result = subprocess.run(
                [self.fastboot_path, "-s", device_id, "getvar", variable],
                capture_output=True,
                text=True
            )
            return result.stdout.strip()
        except Exception as e:
            self.logger.error(f"Error getting device info: {e}")
            return None
