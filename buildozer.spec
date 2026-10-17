[app]
title = PyBrowser Mobile
package.name = pybrowsermobile
package.domain = org.pybrowser

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Gerekli kütüphaneler ve WebView modülü
requirements = python3,kivy==2.3.0,https://github.com/kivy-garden/webview/archive/refs/heads/master.zip

orientation = portrait
fullscreen = 0

# İnternet izni
android.permissions = INTERNET

# --- ÖNEMLİ DERLEME AYARLARI ---
# Lisansları otomatik kabul et
android.accept_sdk_license = True
# Kararlı API ve build-tools sürümlerini sabitle (aidl hatasını önler)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.0
android.archs = arm64-v8a,armeabi-v7a

# WebView kullanımı için gerekli
bootstrap = webview
