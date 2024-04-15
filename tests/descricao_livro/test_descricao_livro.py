from src.livro.livro import Livro


def test_descricao_livro(capsys):
    livro = Livro("Test title", "Test author", 200)
    print(livro)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "O livro Test title de Test author possui 200 páginas.\n"
    )
