/*
 * Copyright (C) 2022 The LineageOS Project
 * Copyright (C) 2022 The XPerience Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#define LOG_TAG "vendor.xperience.touch@1.0-service.lisa"

#include <android-base/logging.h>
#include <hidl/HidlTransportSupport.h>

#include "HighTouchPollingRate.h"

using ::vendor::xperience::touch::V1_0::IHighTouchPollingRate;
using ::vendor::xperience::touch::V1_0::implementation::HighTouchPollingRate;

int main() {
    android::sp<IHighTouchPollingRate> highTouchPollingRate = new HighTouchPollingRate();

    android::hardware::configureRpcThreadpool(1, true);

    if (highTouchPollingRate->registerAsService() != android::OK) {
        LOG(ERROR) << "Cannot register touch high polling rate HAL service.";
        return 1;
    }

    LOG(INFO) << "Touch HAL service ready.";

    android::hardware::joinRpcThreadpool();

    LOG(ERROR) << "Touch HAL service failed to join thread pool.";
    return 1;
}
