#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ADB Manager Module
Handles all ADB operations for Android devices
"""

import subprocess
import logging
from typing import List, Dict, Optional, Tuple
import re

class ADBManager:
    """Manages ADB connections and operations"""
    
    def __init__(self, adb_path: str = "adb"):
        self.adb_path = adb_path
        self.logger = logging.getLogger(self.__class__.__name__)
        self.connected_devices = []
    
    def get_devices(self) -> List[Dict[str, str]]:
        """Get list of connected devices"""
        try:
            result = subprocess.run(
                [self.adb_path, "devices"],
                capture_output=True,
                text=True
            )
            devices = []
            for line in result.stdout.split('\n')[1:]:
                if line.strip() and not line.startswith("List of"):
                    parts = line.split()
                    if len(parts) >= 2:
                        devices.append({
                            "device_id": parts[0],
                            "status": parts[1]
                        })
            self.connected_devices = devices
            return devices
        except Exception as e:
            self.logger.error(f"Error getting devices: {e}")
            return []
    
    def push_file(self, device_id: str, local_path: str, remote_path: str) -> bool:
        """Push file to device"""
        try:
            subprocess.run(
                [self.adb_path, "-s", device_id, "push", local_path, remote_path],
                check=True
            )
            self.logger.info(f"File pushed: {local_path} -> {remote_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error pushing file: {e}")
            return False
    
    def pull_file(self, device_id: str, remote_path: str, local_path: str) -> bool:
        """Pull file from device"""
        try:
            subprocess.run(
                [self.adb_path, "-s", device_id, "pull", remote_path, local_path],
                check=True
            )
            self.logger.info(f"File pulled: {remote_path} -> {local_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error pulling file: {e}")
            return False
    
    def shell_command(self, device_id: str, command: str) -> Tuple[bool, str]:
        """Execute shell command on device"""
        try:
            result = subprocess.run(
                [self.adb_path, "-s", device_id, "shell", command],
                capture_output=True,
                text=True
            )
            return True, result.stdout
        except Exception as e:
            self.logger.error(f"Error executing shell command: {e}")
            return False, str(e)
    
    def install_app(self, device_id: str, apk_path: str) -> bool:
        """Install APK on device"""
        try:
            subprocess.run(
                [self.adb_path, "-s", device_id, "install", apk_path],
                check=True
            )
            self.logger.info(f"App installed: {apk_path}")
            return True
        except Exception as e:
            self.logger.error(f"Error installing app: {e}")
            return False
    
    def uninstall_app(self, device_id: str, package_name: str) -> bool:
        """Uninstall app from device"""
        try:
            subprocess.run(
                [self.adb_path, "-s", device_id, "uninstall", package_name],
                check=True
            )
            self.logger.info(f"App uninstalled: {package_name}")
            return True
        except Exception as e:
            self.logger.error(f"Error uninstalling app: {e}")
            return False
    
    def reboot(self, device_id: str, mode: str = "system") -> bool:
        """Reboot device"""
        try:
            if mode == "bootloader":
                subprocess.run(
                    [self.adb_path, "-s", device_id, "reboot", "bootloader"],
                    check=True
                )
            elif mode == "recovery":
                subprocess.run(
                    [self.adb_path, "-s", device_id, "reboot", "recovery"],
                    check=True
                )
            else:
                subprocess.run(
                    [self.adb_path, "-s", device_id, "reboot"],
                    check=True
                )
            self.logger.info(f"Device rebooted: {device_id} (mode: {mode})")
            return True
        except Exception as e:
            self.logger.error(f"Error rebooting device: {e}")
            return False
