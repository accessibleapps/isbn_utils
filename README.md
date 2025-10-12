# isbn_utils

ISBN validation and extraction for Python.

## What it does

- Validates ISBN-10 and ISBN-13 numbers using proper check digit algorithms
- Extracts ISBNs from arbitrary text
- Handles common formatting (hyphens, URN prefixes)

## Installation

```bash
pip install isbn_utils
```

Or with uv:

```bash
uv add isbn_utils
```

## Usage

### Validate an ISBN

```python
from isbn_utils import isbn_valid

isbn_valid("074348858X")         # True (ISBN-10)
isbn_valid("978-0743488587")     # True (ISBN-13, with hyphens)
isbn_valid("9780743488587")      # True (ISBN-13)
isbn_valid("0743488589")         # False (invalid check digit)
isbn_valid(None)                 # False
```

### Extract ISBN from text

```python
from isbn_utils import find_isbn_in_text

text = "The book's ISBN is 978-0743488587 and costs $20"
find_isbn_in_text(text)  # "9780743488587"

# Returns None if no valid ISBN found
find_isbn_in_text("No ISBN here")  # None
```

### Validate specific formats

```python
from isbn_utils import isbn10_valid, isbn13_valid

isbn10_valid("074348858X")      # True
isbn13_valid("9780743488587")   # True
```

### Clean ISBN formatting

```python
from isbn_utils import clean_isbn

clean_isbn("978-0-7434-8858-7")         # "9780743488587"
clean_isbn("urn:isbn:978-0743488587")  # "9780743488587"
```

## How validation works

**ISBN-10**: Uses modulo 11 check digit algorithm. The last digit can be 0-9 or X (representing 10).

**ISBN-13**: Uses modulo 10 check digit algorithm with alternating weights (1 and 3).

Both implementations follow the official ISBN specification.

## Requirements

- Python 3.8+
- No external dependencies

## Development

```bash
# Clone and setup
git clone https://github.com/accessibleapps/isbn_utils.git
cd isbn_utils

# Install with dev dependencies
uv sync --dev

# Run tests
uv run pytest

# Type checking
uv run pyright

# Linting
uv run ruff check
uv run ruff format
```

## License

MIT License - see LICENSE file for details.
