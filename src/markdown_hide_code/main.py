from markdown.extensions import Extension
from markdown.extensions.attr_list import AttrListExtension
from pymdownx.superfences import SuperFencesCodeExtension


def _custom_formatter(*args, **kwargs):
    return "<div style='display:none;'></div>"


def _custom_validator(language, inputs, options, attrs, md) -> bool:
    if "hide" in inputs and inputs["hide"] == "hide":
        attrs["hide"] = True
        return True
    return False


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

        superfences_extension.superfences.append(
            {
                "name": "markdown_hide_code",
                "test": lambda _: True,
                "formatter": _custom_formatter,
                "validator": _custom_validator,
            }
        )


def makeExtension(**kwargs):
    return HideCodeExtension(**kwargs)
