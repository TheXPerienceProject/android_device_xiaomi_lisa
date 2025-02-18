#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/lisa',
    'hardware/qcom-caf/sm8350',
    'hardware/qcom-caf/wlan',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys/display',
    'vendor/qcom/opensource/commonsys-intf/display',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/opensource/display',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'libmmosal',
        'libdmabufheap',
        'vendor.qti.hardware.wifidisplaysession@1.0',
        'vendor.qti.imsrtpservice@3.0',
        'vendor.xiaomi.hardware.mlipay@1.0',
        'vendor.xiaomi.hardware.displayfeature@1.0'
        'vendor.xiaomi.hardware.mtdservice@1.0'
    ): lib_fixup_vendor_suffix,
    (
        'libOmxCore',
        'libwpa_client',
    ): lib_fixup_remove,
}

blob_fixups: blob_fixups_user_type = {
    ('system_ext/lib/libwfdservice.so', 'system_ext/lib64/libwfdservice.so'): blob_fixup()
        .replace_needed('android.media.audio.common.types-V2-cpp.so', 'android.media.audio.common.types-V3-cpp.so'),
    'system_ext/lib64/libwfdnative.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so')
        .add_needed('libbinder_shim.so')
        .add_needed('libinput_shim.so'),
    ('vendor/etc/media_lahaina/video_system_specs.json', 'vendor/etc/media_shima_v1/video_system_specs.json', 'vendor/etc/media_yupik_v1/video_system_specs.json'): blob_fixup()
        .regex_replace('"max_retry_alloc_output_timeout": 10000,', '"max_retry_alloc_output_timeout": 0,'),
    'vendor/etc/vintf/manifest/c2_manifest_vendor.xml': blob_fixup()
        .regex_replace('.*ozoaudio.*\n?', ''),
    'vendor/lib64/android.hardware.secure_element@1.0-impl.so': blob_fixup()
        .remove_needed('android.hidl.base@1.0.so'),
    ('vendor/etc/camera/pureShot_parameter.xml', 'vendor/etc/camera/pureView_parameter.xml'): blob_fixup()
        .regex_replace(r'=(\d+)>', r'="\1">'),
    'vendor/lib64/hw/camera.xiaomi.so': blob_fixup()
        .sig_replace('29 07 00 94', '1F 20 03 D5'),
    'vendor/lib64/hw/camera.qcom.so': blob_fixup()
        .binary_regex_replace(b'\x73\x74\x5F\x6C\x69\x63\x65\x6E\x73\x65\x2E\x6C\x69\x63', b'\x63\x61\x6D\x65\x72\x61\x5F\x63\x6E\x66\x2E\x74\x78\x74'),
    'vendor/lib64/libwa_sat.so': blob_fixup()
        .binary_regex_replace(b'/system/lib64/', b'/vendor/lib64/'),
        # or use seed xd sed -i 's/\/system\/lib64\([^\/]\)/\/vendor\/lib64\1/g' "${2}"
    'vendor/lib64/hw/displayfeature.default.so': blob_fixup()
        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/bin/hw/vendor.dolby.hardware.dms@2.0-service': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so'),
    'vendor/lib/libcodec2_hidl@1.0_vendor.so': blob_fixup()
        .fix_soname()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_vendor.so'),
    'vendor/lib/libcodec2_vndk_vendor.so': blob_fixup()
        .fix_soname()
        .add_needed('libui_shim.so'),
    'vendor/lib/c2.dolby.client.so': blob_fixup()
        .replace_needed('libcodec2_vndk.so', 'libcodec2_vndk_vendor.so')
        .replace_needed('libcodec2_hidl@1.0.so', 'libcodec2_hidl@1.0_vendor.so'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),
    #('vendor/lib/libstagefright_soft_ac4dec.so', 'vendor/lib/libstagefright_soft_ddpdec.so', 'vendor/lib/libstagefrightdolby.so', 'vendor/lib64/libdlbdsservice.so', 'vendor/lib64/libstagefright_soft_ac4dec.so', 'vendor/lib64/libstagefright_soft_ddpdec.so', 'vendor/lib64/libstagefrightdolby.so'): blob_fixup()
#        .replace_needed('libstagefright_foundation.so', 'libstagefright_foundation-v33.so'),
    'vendor/etc/seccomp_policy/atfwd@2.0.policy': blob_fixup()
        .add_line_if_missing('gettid: 1'),
    'vendor/lib/hw/audio.primary.lisa.so': blob_fixup()
        .binary_regex_replace(b'/vendor/lib/liba2dpoffload\\.so', b'liba2dpoffload_lisa.so\x00\x00\x00\x00\x00\x00\x00')
        .binary_regex_replace(b'/vendor/lib64/liba2dpoffload\\.so', b'liba2dpoffload_lisa.so\x00\x00\x00\x00\x00\x00\x00')
        .binary_regex_replace(b'/vendor/lib/libssrec\\.so', b'libssrec_lisa.so\x00\x00\x00\x00\x00\x00\x00'),
}  # fmt: skip

module = ExtractUtilsModule(
    'lisa',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
