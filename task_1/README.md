# Задание 1

Вы написали view-функцию, обрабатывающую URL `/new_post/`, которая на **GET** запрос отвечает страницей с формой, а на **POST** - создает новый пост из данных формы и редиректит на главную страницу.  
Опишите юнит-тесты, которые вы бы написали для этой view-функции.  

В этом задании код писать не нужно, опишите что по вашему мнению тут нужно/можно протестировать, и почему это нужно сделать именно так, как вы предлагаете.

1. Проверил бы доступность ресурсов при GET и POST запросе. Таким образом поймем, доступен ли ресурс с соответствие с ТЗ
2. Проверил бы, чтобы не обрабатывались другие виды http запросов. Студент может забыть ограничить обработку двумя методами.
3. При GET запросе:
- убедился бы, что возращается код 200. Так убедимся, что есть url и обработчик get запроса.
- Если используется шаблон для возрата страницы с пустой формой, убедился бы, что возвращается именно страница шаблона. 
- Проверил бы, что внутри страницы есть объект формы. Так убедимся, что студент встроил форму в ответ запроса
- Проверил бы, что форма пустая, а не возращается с заполненными данными от какого то другого объекта.
8. При POST запросе:
- проверил бы, что форма позволяет отправить лишь те типы данных, что ей разрешены в полях.
- Убедился бы, что при отправке заполненной формы возвращается код 201. Так поймем на общем уровне, что view функция настроена на обработку пост запроса.
- Проверил бы, что при отправке формы создается объект в БД. Так поймем, сделал ли студент обработку данных формы и сохранение данных в БД
- У самого нового объекта в БД проверил бы соответствие данных тем, что мы отправляли в POST запросе. Так поймем, сохарняет ли студент в новую запись в БД или отправляет данные в имеющуюся.
- Проверил бы, что существует редирект на главную страницу после успешного пост запроса. 