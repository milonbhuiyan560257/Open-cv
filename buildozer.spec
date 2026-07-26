[app]

title = OpenCV Image Demo

package.name = opencvdemo
package.domain = org.milonbhuiyan

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,txt

version = 0.1

requirements = python3,kivy,numpy,opencv

orientation = portrait

fullscreen = 0

android.permissions = INTERNET,CAMERA

android.api = 34

android.minapi = 24

android.ndk = 28c

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2

warn_on_root = 1
