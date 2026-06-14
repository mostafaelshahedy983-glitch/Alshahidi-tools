#!/bin/bash

# الشهيدي تولز - نص التثبيت
# Alshahidi Tools Installation Script

set -e

echo "🚀 الشهيدي تولز - Alshahidi Tools Installer"
echo "=================================="
echo ""

# التحقق من Python
echo "✓ التحقق من Python..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 غير مثبت. يرجى تثبيته أولاً"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "  - Python $PYTHON_VERSION مثبت"
echo ""

# التحقق من pip
echo "✓ التحقق من pip..."
if ! command -v pip3 &> /dev/null; then
    echo "✗ pip3 غير مثبت. يرجى تثبيته أولاً"
    exit 1
fi

# التحقق من ADB
echo "✓ التحقق من ADB..."
if ! command -v adb &> /dev/null; then
    echo "⚠ ADB غير مثبت. يمكن تثبيته بـ:"
    echo "  Ubuntu/Debian: sudo apt-get install adb"
    echo "  Fedora: sudo dnf install adb"
    echo "  Arch: sudo pacman -S android-tools"
else
    ADB_VERSION=$(adb version | head -1)
    echo "  - $ADB_VERSION"
fi
echo ""

# تثبيت المتطلبات
echo "✓ تثبيت المتطلبات..."
pip3 install -r requirements.txt
echo "  - تم تثبيت جميع المتطلبات"
echo ""

# إنشاء المجلدات
echo "✓ إنشاء المجلدات..."
mkdir -p ~/.alshahidi_tools/backups
mkdir -p ~/.alshahidi_tools/logs
mkdir -p ~/.alshahidi_tools/roms
echo "  - تم إنشاء المجلدات"
echo ""

# جعل main.py قابل للتنفيذ
chmod +x cli/main.py
echo "✓ تم جعل البرنامج قابل للتنفيذ"
echo ""

# إنشاء رابط رمزي (اختياري)
if [ -w "/usr/local/bin" ]; then
    ln -sf "$(pwd)/cli/main.py" /usr/local/bin/alshahidi
    echo "✓ تم إنشاء رابط /usr/local/bin/alshahidi"
    echo "  - يمكنك الآن تشغيل: alshahidi --help"
else
    echo "⚠ لا يمكن إنشاء رابط في /usr/local/bin (تحتاج صلاحيات)"
    echo "  - شغل: sudo ln -sf \"$(pwd)/cli/main.py\" /usr/local/bin/alshahidi"
fi
echo ""

echo "=================================="
echo "✅ تم التثبيت بنجاح!"
echo "=================================="
echo ""
echo "الاستخدام:"
echo "  python3 cli/main.py --help"
echo "  python3 cli/main.py devices list"
echo "  python3 cli/main.py flash rom DEVICE_ID ROM_PATH"
echo ""
