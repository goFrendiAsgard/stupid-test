# Useless test

This test brings no value, but I do it anyway because of TDD.

# Prerequisites

- Python
- venv

# How to run

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pytest
```

# About the code

## Acceptance criteria

```
When hello_world function is executed, a `Hello World!` should be appeared on the screen.
```

## How to write the code

First, you start with the test. Because we want to do TDD:

```python
def test_hello_world(capfd):
    hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
```

Next, you run the test, and it should fail:

```bash
pytest
```

Once you confirm that the test failed, you start implementing `hello_world`. Now your code looks like this:

```bash
def hello_world():
    print("Hello World!")


def test_hello_world(capfd):
    hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
```

You run the test again, and it should pass:

```bash
pytest
```

# This is satire

No one does this in the real world, and for a single good reason: The test brings no value at all.

Some other reasons why not doing this:

- The test is harder to maintain than the implementation
- The implementation is clear enough

The test will bring more value if:

- Your implementation is going to be updated/changed/refactored frequently.
- You have multiple scenarios, and running the test will run all the scenarios faster than doing it manually.


## A better approach

Don't try to test the `print` function, it is part of the language, and it has been tested by the PSF.

Instead, make a function that returns a hello world, and test the return value.

```python
def hello_world() -> str:
    return "Hello World!"


def test_hello_world():
    assert hello_world() == "Hello World!"


if __name__ == '__main__':
    print(hello_world())
```

Simpler, but still brings no value.


## Another scenario where tests make sense

You have multiple scenarios

```python
import sys

def hello(name: str) -> str:
    return f"Hello {name}"


def test_hello_with_bob_as_name():
    assert hello('Bob') == "Hello Bob"


def test_hello_with_spongebob_as_name():
    assert hello('Spongebob') == "Hello Spongebob"


if __name__ == '__main__':
    print(hello(sys.argv[1]))
```

This test brings more value to your system.

Rather than doing this:

```bash
python program.py Bob
python program.py Spongebob
```

You can simply run:

```bash
pytest
```

It will run both scenarios described in the test.

