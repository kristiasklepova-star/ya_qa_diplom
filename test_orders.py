import pytest
from order_api import create_order, get_order_by_track
from data import default_order

def test_create_order_returns_success():
    """Тест 1: Проверка успешного создания заказа."""
    response = create_order(default_order)
    assert response.status_code in (200, 201), \
        f"Ошибка создания заказа: {response.status_code} - {response.text}"

def test_create_order_returns_track():
    """Тест 2: Проверка наличия трека в ответе при создании заказа."""
    # Создаём заказ
    response = create_order(default_order)
    assert response.status_code in (200, 201), \
        "Не удалось создать заказ для проверки трека"
    
    # Проверяем наличие трека
    response_body = response.json()
    track = response_body.get("track")
    assert track is not None, "Ответ не содержит поле 'track'"

def test_get_order_by_track_returns_success():
    """Тест 3: Проверка успешного получения заказа по треку."""
    # Сначала создаём заказ, чтобы получить трек
    create_response = create_order(default_order)
    assert create_response.status_code in (200, 201), \
        "Не удалось создать заказ для проверки получения по треку"
    
    track = create_response.json().get("track")
    assert track is not None, "Не удалось получить трек из ответа"
    
    # Получаем заказ по треку
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, \
        f"Ожидался код 200, получен {get_response.status_code} - {get_response.text}"
    
    # Дополнительно проверяем, что ответ не пустой
    order_data = get_response.json()
    assert order_data is not None, "Получен пустой ответ при запросе заказа"