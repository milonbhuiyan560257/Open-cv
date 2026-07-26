[app]

# (str) Title of your application
title = OpenCV Image Demo

# (str) Package name
package.name = opencvdemo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.milonbhuiyan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# IMPORTANT: opencv-python must be here for your OpenCV app to work!
requirements = python3,kivy==2.2.1,numpy,opencv-python,android

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse, landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

#
# OSX Specific
#

# change the major version of python used by the app
osx.python_version = 3.10

# Kivy version to use
osx.kivy_version = 2.2.1

#
# Android specific
#

# (list) Permissions
# NOTE: Camera permission needed for OpenCV camera features
android.permissions = INTERNET, CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) The Android archs to build for
# Choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
