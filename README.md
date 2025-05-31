# markdown-hide-code

An small extension for Python's [Markdown](https://pypi.org/project/Markdown/) library that
hides code blocks marked with `hide` from the markdown output. This is useful
when developers want to include unit tests in their markdown documentation (e.g., using [pytest-markdown-docs](https://github.com/modal-labs/pytest-markdown-docs/)) but don't want those tests to be visible to documentation readers. I created this extension while developing [Pyoframe](https://bravos-power.github.io/pyoframe/).

~~~
```python {hide}
# This code block will be hidden in the rendered markdown.
```
~~~

## Install

`pip install markdown-hide-code`

## Usage with [`mkdocs`](https://www.mkdocs.org/)

Add the extension to your `mkdocs.yml` configuration:

```yml
markdown_extensions:
  ...
  - pymdownx.superfences
  - attr_list
  - markdown_hide_code  # must appear after superfences and attr_list
    ...
```
> [!WARNING]
> [`pymdownx.superfences`](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) and [`attr_list`](https://python-markdown.github.io/extensions/attr_list/) are required dependencies and must be listed **BEFORE** `markdown-hide-code`.

Then, to hide a code block simply add `{hide}`:

~~~
```python {hide}
# This code block will be hidden in the output
```
~~~

## Usage directly with the [Markdown](https://pypi.org/project/Markdown/) library

Just add the extension to the list. Order matters (see above warning).

```python
from markdown import Markdown

md = Markdown(extensions=["pymdownx.superfences", "attr_list", "markdown_hide_code"])
...
```

### Notes for contributors (and myself)

Clone the repo and run [`uv sync`](https://docs.astral.sh/uv) and `pre-commit install` to get setup. The core code is all found in `src/markdown_hide_code/main.py`.