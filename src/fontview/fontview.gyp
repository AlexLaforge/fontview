{
  'targets': [
    {
      'target_name': 'fontview',
      'type': 'executable',
      'sources': [
        'caret.cpp',
        'font_style.cpp',
        'font_var_axis.cpp',
        'main.cpp',
        'name_table.cpp',
        'sample_text.cpp',
        'text_settings.cpp',
      ],
      'include_dirs': [
        '..',
      ],
      'defines': [
        'FONTVIEW_VERSION=' + '<!(echo $FONTVIEW_VERSION)',
      ],
      'dependencies': [
        '../third_party/freetype/freetype.gyp:freetype',
        '../third_party/fribidi/fribidi.gyp:fribidi',
        '../third_party/harfbuzz/harfbuzz.gyp:harfbuzz',
        '../third_party/raqm/raqm.gyp:raqm',
        '../third_party/wxWidgets/wxWidgets.gyp:core',
      ],
      'conditions': [
        ['OS == "mac"', {
          'sources': [
            'mac/caret.mm',
          ],
          'link_settings': {
            'libraries': [
              '$(SDKROOT)/System/Library/Frameworks/Foundation.framework',
            ],
          },
        }],
      ],
    },
  ],
  'target_defaults': {
    'xcode_settings': {
      'GCC_VERSION': 'com.apple.compilers.llvm.clang.1_0',
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++14',
      'CLANG_CXX_LIBRARY': 'libc++',
    },
  },
}
