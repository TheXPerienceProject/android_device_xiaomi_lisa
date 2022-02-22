/*
 * Copyright (C) 2022 The LineageOS Project
 * Copyright (C) 2022 The XPerience Project
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#pragma once

#include <vendor/xperience/touch/1.0/IHighTouchPollingRate.h>

namespace vendor {
namespace xperience {
namespace touch {
namespace V1_0 {
namespace implementation {

using ::android::hardware::Return;

class HighTouchPollingRate : public IHighTouchPollingRate {
  public:
    // Methods from ::vendor::xperience::touch::V1_0::IHighTouchPollingRate follow.
    Return<bool> isEnabled() override;
    Return<bool> setEnabled(bool enabled) override;
};

}  // namespace implementation
}  // namespace V1_0
}  // namespace touch
}  // namespace xperience
}  // namespace vendor
