#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alshahidi Tools - Main CLI Entry Point
"""

import click
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger('AlshahidiTools')

@click.group()
@click.version_option(version='1.0.0')
def cli():
    """الشهيدي تولز - Alshahidi Tools
    
    أداة شاملة لإدارة وصيانة وتفليش أجهزة Android
    Comprehensive Android device management and flashing tool
    """
    pass

@cli.group()
def devices():
    """Device management commands"""
    pass

@devices.command()
def list():
    """List connected devices"""
    from core.device_detector import DeviceDetector
    detector = DeviceDetector()
    devices = detector.detect_all_devices()
    
    if not devices:
        click.echo(click.style("❌ No devices found", fg='red'))
        return
    
    click.echo(click.style("📱 Connected Devices:\n", fg='green', bold=True))
    for device in devices:
        click.echo(f"  • ID: {device.get('device_id')}")
        click.echo(f"    Model: {device.get('model', 'Unknown')}")
        click.echo(f"    Manufacturer: {device.get('manufacturer', 'Unknown')}")
        click.echo(f"    Mode: {device.get('mode', 'unknown')}")
        click.echo()

@cli.group()
def flash():
    """Flashing commands"""
    pass

@flash.command()
@click.option('--device', '-d', required=True, help='Device ID')
@click.option('--rom', '-r', required=True, type=click.Path(exists=True), help='ROM file path')
def rom(device, rom):
    """Flash ROM to device"""
    from modules.flashing_engine import FlashingEngine
    
    click.echo(click.style("🚀 Starting ROM flash...", fg='cyan'))
    engine = FlashingEngine()
    
    # Validate ROM
    valid, message = engine.validate_rom(rom)
    if not valid:
        click.echo(click.style(f"❌ {message}", fg='red'))
        return
    
    click.echo(click.style("✅ ROM validated", fg='green'))
    click.echo(click.style(f"🔧 Flashing to device: {device}", fg='yellow'))
    # Flash implementation

@cli.group()
def backup():
    """Backup commands"""
    pass

@backup.command()
@click.option('--device', '-d', required=True, help='Device ID')
def create(device):
    """Create device backup"""
    from modules.backup_restore import BackupRestore
    
    click.echo(click.style(f"💾 Creating backup for device: {device}", fg='cyan'))
    br = BackupRestore()
    backup_path = br.backup_device(device)
    
    if backup_path:
        click.echo(click.style(f"✅ Backup created: {backup_path}", fg='green'))
    else:
        click.echo(click.style("❌ Failed to create backup", fg='red'))

@backup.command()
def list():
    """List available backups"""
    from modules.backup_restore import BackupRestore
    
    br = BackupRestore()
    backups = br.list_backups()
    
    if not backups:
        click.echo(click.style("No backups found", fg='yellow'))
        return
    
    click.echo(click.style("📁 Available Backups:\n", fg='green', bold=True))
    for backup in backups:
        click.echo(f"  • {backup}")

def main():
    """Main entry point"""
    try:
        cli()
    except Exception as e:
        click.echo(click.style(f"❌ Error: {str(e)}", fg='red'), err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()
