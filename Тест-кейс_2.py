
Название:	   Проверка итоговой стоимости при оформлении заказа
Предусловия:   Установлен Firefox, 
               geckodriver, 
               библиотека selenium, 
               созданы классы страниц: LoginPage, InventoryPage, CartPage, CheckoutPage.

Браузер:	   Firefox


Шаг	                                               Метод Page Object	                                      Ожидаемый результат
1	Открыть сайт магазина	                       login_page.open()	                                      Загружена страница авторизации
2	Авторизоваться как standard_user	           login_page.login("standard_user", "secret_sauce")	      Открыта главная страница с товарами
3	Добавить в корзину Sauce Labs Backpack	       inventory_page.add_backpack()	                          Товар добавлен, у иконки корзины счётчик "1"
4	Добавить в корзину Sauce Labs Bolt T-Shirt	   inventory_page.add_bolt_tshirt()	                          Товар добавлен, счётчик корзины "2"
5	Добавить в корзину Sauce Labs Onesie	       inventory_page.add_onesie()	                              Товар добавлен, счётчик корзины "3"
6	Перейти в корзину	                           inventory_page.go_to_cart()	                              Открыта страница корзины, видны три товара
7	Нажать кнопку Checkout	                       cart_page.checkout()	                                      Открыта форма оформления заказа
8	Заполнить форму: имя, фамилия, индекс	       checkout_page.fill_form("Максим", "Тараканов", "669900")	  Поля заполнены данными
9	Нажать кнопку Continue	                       checkout_page.continue_to_overview()	                      Открыта страница с итогами заказа
10	Прочитать итоговую стоимость (Total)	       checkout_page.get_total()	                              Возвращена строка с итоговой суммой
11	Проверить, что итоговая сумма равна $58.29	   assert total == "Total: $58.29"	                          Тест проходит успешно