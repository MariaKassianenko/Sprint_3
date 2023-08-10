from locators import *
import data_for_sb_tests as data
import urls


class TestConstuctor():
    def test_switch_ingredients_bread(self, user):  # работают переходы к разделам - Булки
        user.get(urls.main_page)
        ingredient = data.ingredients.get('bread')
        ingredient_locator = user.find_element(*ingredients_locator(ingredient))
        user.execute_script("arguments[0].scrollIntoView();", ingredient_locator)
        ingredient_locator.click()
        assert 'current' in user.find_element(*current_ingredient_locator(ingredient)).get_attribute('class')

    def test_switch_ingredients_sauses(self, user):  # работают переходы к разделам - Соусы
        user.get(urls.main_page)
        ingredient = data.ingredients.get('sauses')
        ingredient_locator = user.find_element(*ingredients_locator(ingredient))
        user.execute_script("arguments[0].scrollIntoView();", ingredient_locator)
        ingredient_locator.click()
        assert 'current' in user.find_element(*current_ingredient_locator(ingredient)).get_attribute('class')

    def test_switch_ingredients_filling(self, user):  # работают переходы к разделам - Начинки
        user.get(urls.main_page)
        ingredient = data.ingredients.get('filling')
        ingredient_locator = user.find_element(*ingredients_locator(ingredient))
        user.execute_script("arguments[0].scrollIntoView();", ingredient_locator)
        ingredient_locator.click()
        assert 'current' in user.find_element(*current_ingredient_locator(ingredient)).get_attribute('class')
