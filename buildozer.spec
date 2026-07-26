[app]

title = OpenCV Image Demo
package.name = opencvdemo
package.domain = org.milonbhuiyan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt
version = 0.1

# IMPORTANT: 'opencv' recipe, NOT 'opencv-python'
requirements = python3,kivy,numpy,opencv

orientation = portrait
fullscreen = 0

osx.python_version = 3.10
osx.kivy_version = 2.2.1

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 1
