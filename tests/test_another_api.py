import requests
import allure


@allure.feature('get status_code')
@allure.story('Пингуем ресурс')
def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    with allure.step("Запрос отправлен, посмотрим код ответа"):
        assert response.status_code == 200, f"Получен код ответа {response.status_code}"

