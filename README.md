# الشهيدي تولز - Alshahidi Tools

**أداة شاملة لإدارة وصيانة وتفليش أجهزة Android**

## المميزات ✨

- ✅ **التفليش الكامل** (ROM, Recovery, Bootloader, Kernel)
- ✅ **دعم MTKClient** لأجهزة MediaTek
- ✅ **دعم Chimera** للتحليل المتقدم
- ✅ **دعم Pandora** لاستخراج البيانات
- ✅ **دعم SP Flash** لأجهزة MTK
- ✅ **إدارة متعددة الأجهزة**
- ✅ **Backup & Restore**
- ✅ **OTA Updates**
- ✅ **App Management**
- ✅ **System Monitoring**
- ✅ **Custom Recovery Installation**
- ✅ **واجهة CLI احترافية**

## المتطلبات 📋

- Python 3.9+
- Linux/Unix
- ADB و Fastboot مثبتة
- USB Driver للأجهزة

## التثبيت 🔧

```bash
git clone https://github.com/mostafaelshahedy983-glitch/Alshahidi-tools.git
cd Alshahidi-tools
pip install -r requirements.txt
chmod +x install.sh
./install.sh
```

## الاستخدام 📖

```bash
python3 main.py
python3 main.py --help
python3 main.py flash --rom path/to/rom.zip
python3 main.py backup --device 12345
python3 main.py restore --backup backup.tar
```

## البنية 📁

```
Alshahidi-tools/
├── core/
│   ├── adb_manager.py
│   ├── fastboot_manager.py
│   ├── mtkclient_handler.py
│   ├── chimera_handler.py
│   ├── pandora_handler.py
│   ├── sp_flash_handler.py
│   └── device_detector.py
├── modules/
│   ├── flashing_engine.py
│   ├── backup_restore.py
│   ├── ota_updater.py
│   ├── app_manager.py
│   └── system_monitor.py
├── cli/
│   ├── main.py
│   ├── commands.py
│   └── utils.py
├── config/
│   ├── settings.json
│   └── devices.json
├── logs/
├── install.sh
├── requirements.txt
└── README.md
```

## الترخيص 📄

GNU General Public License v3.0

## المطور 👨‍💻

Mostafa Elshahedy

## الدعم 🤝

للمشاكل والاقتراحات: https://github.com/mostafaelshahedy983-glitch/Alshahidi-tools/issues
