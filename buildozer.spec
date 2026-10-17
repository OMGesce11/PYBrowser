[app]
title = Kivy Browser
package.name = kivybrowser
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy==2.3.0,https://github.com/kivy-garden/webview/archive/refs/heads/master.zip

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

bootstrap = webview
