def hello_world():
    print("Hello World!")


def test_hello_world(capfd):
    hello_world()
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
