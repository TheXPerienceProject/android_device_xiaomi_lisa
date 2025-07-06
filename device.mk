#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8350-common
$(call inherit-product, device/xiaomi/sm8350-common/common.mk)


PRODUCT_PACKAGES += \
    Aperture

# Properties
PRODUCT_ODM_PROPERTIES += \
    ro.com.google.lens.oem_camera_package=com.android.camera \
    persist.vendor.camera.privapp.list=org.codeaurora.snapcam,com.android.camera \
    ro.miui.notch=1 \
    ro.product.mod_device=lisa

PRODUCT_ODM_PROPERTIES += \
    camera.disable_zsl_mode=1 \
    ro.hardware.camera=xiaomi

# Overlays
DEVICE_PACKAGE_OVERLAYS += \
    $(LOCAL_PATH)/overlay

# Overlays-RRO
PRODUCT_PACKAGES += \
    lisaCNSettingsProviderOverlay \
    lisaCNWifiOverlay \
    lisaGLSettingsProviderOverlay \
    lisaGLWifiOverlay \
    lisaINSettingsProviderOverlay \
    lisaINWifiOverlay \
    LisaNfcOverlay \
    LisaRegulatory2109119dc \
    LisaRegulatory2109119dg \
    LisaRegulatory2109119di \
    LisaSettingsOverlay

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# Audio
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/audio/audio_platform_info_yupikqrd.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/audio_platform_info_yupikqrd.xml \
    $(LOCAL_PATH)/audio/mixer_paths_yupikqrd.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/mixer_paths_yupikqrd.xml \
    $(LOCAL_PATH)/audio/mixer_paths_overlay_dynamic.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/mixer_paths_overlay_dynamic.xml \
    $(LOCAL_PATH)/audio/mixer_paths_overlay_static.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/mixer_paths_overlay_static.xml \
    $(LOCAL_PATH)/audio/sound_trigger_mixer_paths_yupikqrd.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/sound_trigger_mixer_paths_yupikqrd.xml \
    $(LOCAL_PATH)/audio/sound_trigger_platform_info.xml:$(TARGET_COPY_OUT_VENDOR)/etc/audio/sku_yupik/sound_trigger_platform_info.xml

# Sku properties
PRODUCT_COPY_FILES += \
    $(call find-copy-subdir-files,*,$(LOCAL_PATH)/sku/,$(TARGET_COPY_OUT_ODM)/etc)

# WiFi Display
PRODUCT_SYSTEM_PROPERTIES += \
    vendor.sys.video.disable.ubwc=1

# Call the proprietary setup
$(call inherit-product, vendor/xiaomi/lisa/lisa-vendor.mk)
