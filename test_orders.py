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
    response = create_order(default_order)
    response_body = response.json()
    track = response_body.get("track")
    
    # Проверяем наличие трека
    # Статус код не проверяем отдельно, но при ошибке создания 
    # track будет None, и assert упадёт с информативным сообщением
    assert track is not None, \
        f"Трек не найден в ответе. Статус: {response.status_code}, тело: {response.text}"

def test_get_order_by_track_returns_success():
    """Тест 3: Проверка успешного получения заказа по треку."""
    # Создаём заказ и получаем трек
    create_response = create_order(default_order)
    create_response_body = create_response.json()
    track = create_response_body.get("track")
    
    # Проверяем, что удалось получить трек (иначе тест не имеет смысла)
    if track is None:
        pytest.fail(f"Не удалось получить трек. Статус: {create_response.status_code}, тело: {create_response.text}")
    
    # Получаем заказ по треку
    get_response = get_order_by_track(track)
    
    # Проверяем успешность получения заказа
    assert get_response.status_code == 200, \
        f"Ожидался код 200, получен {get_response.status_code} - {get_response.text}"