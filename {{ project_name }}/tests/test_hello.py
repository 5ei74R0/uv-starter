from {{ project_name }}.hello import main


def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from" in captured.out
