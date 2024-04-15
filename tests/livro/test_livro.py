from src.livro.livro import Livro


def test_cria_livro():
    livro = Livro("Test title", "Test author", 200)
    assert livro.titulo == "Test title"
    assert livro.autor == "Test author"
    assert livro.paginas == 200
