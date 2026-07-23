[app]

# (str) Title of your application
title = OpenCV Image Classifier

# (str) Package name
package.name = myopencvapp

# (str) Package domain
package.domain = org.test

# (str) Application version
version = 0.1

# (str) Source code directory
source.dir = .

# (list) Source files
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Note: kivy==2.2.1, opencv, numpy==1.26.4 নির্দিষ্ট করে দেওয়া হলো
requirements = python3,kivy==2.2.1,opencv,numpy==1.26.4

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen option
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA, INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API support (NumPy-এর জন্য সর্বনিম্ন 24 বাধ্যতামূলক)
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (bool) Accept NDK license
android.accept_sdk_license = True

# (str) Architecture
android.archs = arm64-v8a

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
