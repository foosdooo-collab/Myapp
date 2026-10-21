[app]

title = My Buildozer App
package.name = mybuildozerapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = .git,.github,.buildozer,bin,venv,.venv

version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android settings
android.permissions = INTERNET
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Build settings
p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 0
