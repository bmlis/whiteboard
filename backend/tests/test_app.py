def test_root_returns_hello(test_app):
    assert test_app.get('/').data == b'Hello World'
