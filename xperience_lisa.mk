#
# Copyright (C) 2022 PixelOS
# Copyright (C) 2022 The XPerience Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from lisa device
$(call inherit-product, device/xiaomi/lisa/device.mk)

# Inherit some common XPerience stuff
$(call inherit-product, vendor/xperience/config/common.mk)
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_SUPPORTS_QUICK_TAP := true

PRODUCT_BRAND := Xiaomi
PRODUCT_DEVICE := lisa
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_NAME := xperience_lisa
PRODUCT_MODEL := Xiaomi 11 Lite 5G NE

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi
