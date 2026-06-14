#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Device Detector Module
Detects and identifies Android devices
"""

import json
import logging
from typing import Dict, Optional, List
from .adb_manager import ADBManager
from .fastboot_manager import FastbootManager

class DeviceDetector:
    """Detects and identifies Android devices"""
    
    def __init__(self):
        self.adb = ADBManager()
        self.fastboot = FastbootManager()
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def detect_all_devices(self) -> List[Dict[str, str]]:
        """Detect all connected devices"""
        adb_devices = self.adb.get_devices()
        fastboot_devices = self.fastboot.get_devices()
        
        devices = []
        
        # Add ADB devices
        for device in adb_devices:
            if device['status'] == 'device':
                info = self._get_device_info(device['device_id'])
                info['device_id'] = device['device_id']
                info['mode'] = 'adb'
                devices.append(info)
        
        # Add Fastboot devices
        for device_id in fastboot_devices:
            devices.append({
                'device_id': device_id,
                'mode': 'fastboot',
                'model': 'Unknown',
                'manufacturer': 'Unknown'
            })
        
        return devices
    
    def _get_device_info(self, device_id: str) -> Dict[str, str]:
        """Get device information via ADB"""
        info = {}
        
        success, model = self.adb.shell_command(device_id, "getprop ro.product.model")
        if success:
            info['model'] = model.strip()
        
        success, manufacturer = self.adb.shell_command(device_id, "getprop ro.product.manufacturer")
        if success:
            info['manufacturer'] = manufacturer.strip()
        
        success, android_version = self.adb.shell_command(device_id, "getprop ro.build.version.release")
        if success:
            info['android_version'] = android_version.strip()
        
        success, build_id = self.adb.shell_command(device_id, "getprop ro.build.id")
        if success:
            info['build_id'] = build_id.strip()
        
        success, serial = self.adb.shell_command(device_id, "getprop ro.serialno")
        if success:
            info['serial'] = serial.strip()
        
        return info
    
    def get_device_type(self, device_id: str) -> str:
        """Determine device type (phone, tablet, etc.)"""
        try:
            success, output = self.adb.shell_command(device_id, "getprop ro.build.characteristics")
            if success:
                characteristics = output.strip()
                if 'tablet' in characteristics.lower():
                    return 'tablet'
                elif 'watch' in characteristics.lower():
                    return 'watch'
                elif 'tv' in characteristics.lower():
                    return 'tv'
            return 'phone'
        except:
            return 'phone'
