import re

import pytest
from markdown import Markdown


@pytest.fixture
def md_with_extension(request):
    return Markdown(
        extensions=["pymdownx.superfences", "attr_list", "markdown_hide_code"]
    )


def test_works(md_with_extension):
    input_md = """
```python { hide }
print("This should be hidden")
```

```python
print("This should be visible")
```
"""
    html = md_with_extension.convert(input_md)
    assert "This should be hidden" not in html
    assert "This should be visible" in html


def test_spacing_does_not_matter(md_with_extension):
    input_md = """
```python {hide}
print("This should be hidden")
```

```python
print("This should be visible")
```
"""
    html = md_with_extension.convert(input_md)
    assert "This should be hidden" not in html
    assert "This should be visible" in html


def test_no_change_without_hide(md_with_extension):
    input_md = """
```python
assert 4 == 4
```
    """
    md_counterfactual = Markdown(extensions=["pymdownx.superfences", "attr_list"])
    assert md_with_extension.convert(input_md) == md_counterfactual.convert(input_md)


def test_raises_when_missing_dependencies():
    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=["pymdownx.superfences", "markdown_hide_code"])

    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=["attr_list", "markdown_hide_code"])


def test_raises_when_dependency_order_is_wrong():
    with pytest.raises(
        ImportError,
        match=re.escape(
            "Extensions 'pymdownx.superfences' and 'attr_list' must be included in your configuration **before** markdown_hide_code."
        ),
    ):
        Markdown(extensions=["markdown_hide_code", "attr_list", "pymdownx.superfences"])
