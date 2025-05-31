import re

import pytest
from markdown import Markdown

from markdown_hide_code import HideCodeExtension


def test_works():
    md = Markdown(extensions=["pymdownx.superfences", "attr_list", HideCodeExtension()])

    input_md = """
```python { hide }
print("This should be hidden")
```

```python
print("This should be visible")
```
"""
    html = md.convert(input_md)
    assert "This should be hidden" not in html
    assert "This should be visible" in html


def test_spacing_does_not_matter():
    md = Markdown(extensions=["pymdownx.superfences", "attr_list", HideCodeExtension()])

    input_md = """
```python {hide}
print("This should be hidden")
```

```python
print("This should be visible")
```
"""
    html = md.convert(input_md)
    assert "This should be hidden" not in html
    assert "This should be visible" in html


def test_raises_when_missing_dependencies():
    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=["pymdownx.superfences", HideCodeExtension()])

    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=["attr_list", HideCodeExtension()])


def test_raises_when_dependency_order_is_wrong():
    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=[HideCodeExtension(), "attr_list", "pymdownx.superfences"])
