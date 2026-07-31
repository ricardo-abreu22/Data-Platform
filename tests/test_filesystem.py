from app.storage.filesystem import FileStorage

def test_save_creates_file(tmp_path):
    storage = FileStorage()

    data = b"Hello World"

    storage.save(
        directory=str(tmp_path),
        filename="hello.txt",
        data=data,
    )

    saved_file = tmp_path / "hello.txt"

    assert saved_file.exists()
    assert saved_file.read_bytes() == data