import functools

from markdown.extensions import Extension
from markdown.extensions.attr_list import AttrListExtension
from pymdownx.superfences import (
    SuperFencesCodeExtension,
    _formatter,
    _validator,
    default_validator,
    fence_code_format,
)


def _custom_formatter(*args, attrs=None, **kwargs):
    if attrs and "hide" in attrs:
        return "<div style='display:none;'></div>"
    return fence_code_format(*args, attrs=attrs, **kwargs)


class HideCodeExtension(Extension):
    """Markdown extension to hide code blocks containing the 'hide' attribute."""

    def extendMarkdown(self, md):
        superfences_extension = None
        attr_extension = None
        for ext in md.registeredExtensions:
            if isinstance(ext, SuperFencesCodeExtension):
                superfences_extension = ext
            elif isinstance(ext, AttrListExtension):
                attr_extension = ext
        if not superfences_extension or not attr_extension:
            raise ImportError(
                "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
            )

        superfences_extension.extend_super_fences(
            name="*",
            formatter=functools.partial(
                _formatter, class_name="", _fmt=_custom_formatter
            ),
            validator=functools.partial(_validator, validator=default_validator),
        )


def makeExtension(**kwargs):
    return HideCodeExtension(**kwargs)
