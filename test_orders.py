import pytest
from order_api import create_order, get_order_by_track
from data import default_order   # импортируем данные напрямую

def test_create_and_get_order():

    # Шаг 1: создание заказа
    create_response = create_order(default_order)
    assert create_response.status_code in (200, 201), \
        f"Ошибка создания заказа: {create_response.status_code} - {create_response.text}"

    # Шаг 2: извлечение трека из ответа
    response_body = create_response.json()
    track = response_body.get("track")
    assert track is not None, "Ответ не содержит поле 'track'"

    # Шаг 3: получение заказа по треку
    get_response = get_order_by_track(track)
    assert get_response.status_code == 200, \
        f"Ожидался код 200, получен {get_response.status_code} - {get_response.text}"

    # (необязательно) Проверка, что в ответе есть данные
    order_data = get_response.json()
    assert order_data is not None, "Получен пустой ответ при запросе заказа"