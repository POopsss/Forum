from ckeditor.configs import DEFAULT_CONFIG

CKEDITOR_UPLOAD_PATH = 'media/uploads'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_ALLOW_NONIMAGE_FILES = True

CKEDITOR_CONFIGS = {
    'default': {
        'height': 100,
        'width': 998,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Smiley', 'TextColor', 'RemoveFormat', ],
        ]
    }
}


# CUSTOM_TOOLBAR = [
#     {
#         'name': 'document',
#         'items': [
#             'Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', '-',
#             'TextColor', 'BGColor', '-',
#             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
#         ],
#     },
#     {
#         'name': 'widgets',
#         'items': [
#             'Undo', 'Redo', '-',
#             'NumberedList', 'BulletedList', '-',
#             'Outdent', 'Indent', '-',
#             'Link', 'Unlink', '-',
#             'Image', 'CodeSnippet', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', '-'
#             'Blockquote', '-',
#             'ShowBlocks', 'Maximize',
#         ],
#     },
# ]


customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]