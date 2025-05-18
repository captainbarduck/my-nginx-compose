from app import app  # импортируем flask-приложение

def test_root_route():
    # создаём тестового клиента Flask
    tester = app.test_client()

    # делаем GET-запрос на главную страницу
    response = tester.get("/")

    # проверяем, что получен статус 200
    assert response.status_code == 200

    # проверяем, что в ответе есть строка "Hello"
    assert b"Hello" in response.data
