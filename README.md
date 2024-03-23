# StepTwo


Этот проект представляет собой веб-сервер, написанный на языке программирования Go. Он предоставляет API для работы с данными клиентов и обработки запросов на получение и сохранение состояния.

Зависимости
Для запуска сервера необходимо установить зависимости для Go. Убедитесь, что у вас установлен Go, затем выполните следующую команду для установки зависимостей: `go mod init sqlite-golang` , `go get`


Для запуска тестов необходимо установить зависимости для Python. Вы можете установить их, выполнив следующую команду:
`pip install requests`
Запуск сервера
Чтобы запустить сервер, выполните следующую команду:
`go run main.go`
После запуска сервер будет доступен по адресу `http://localhost:3001``.

Запуск тестов
Для запуска тестов перейдите в папку test и выполните следующую команду:
`python test_script.py`
Данные тестов можно легко менять для себя)
Это запустит скрипт тестирования test_script.py, который будет тестировать функциональность сервера.