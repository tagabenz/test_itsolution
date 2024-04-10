Для запуска контейнера в Docker:
`docker build -t it_solution .`
`docker run --rm -p 8000:8000 -v $PWD:/app it_solution`

доступ по адресу localhost:8000
