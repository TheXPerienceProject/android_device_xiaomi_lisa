#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from lisa device
$(call inherit-product, device/xiaomi/lisa/device.mk)

# Inherit some common XPerience stuff
$(call inherit-product, vendor/xperience/config/common.mk)

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := lisa
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_MODEL := 2109119DG
PRODUCT_NAME := xperience_lisa

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    PRODUCT_NAME=lisa_global \
    BuildDesc="lisa_global-user 14 UKQ1.231108.001 V816.0.10.0.UKOMIXM release-keys" \
    BuildFingerprint=Xiaomi/lisa_global/lisa:14/UKQ1.231108.001/V816.0.10.0.UKOMIXM:user/release-keys

XPERIENCE_MAINTAINER := Kισżż
#XPERIENCE_CHIPSET := "Snapdragon 778G"
XPERIENCE_BATTERY := 4250mAh
XPERIENCE_DISPLAY := 1080x2400
TARGET_STOCK_GAPPS := true
WITH_GMS:=true
#TARGET_ESSENTIAL_GAPPS := true
TARGET_ENABLE_PIXEL_GOODIES := true
