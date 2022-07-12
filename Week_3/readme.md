Для запуска `hm3_task_1.py` с использованием Redis необходимо выполнить следующие команды:
```sh
pip install --upgrade pip
pip install -r requirements.txt
docker build -t redis_loc .
docker run -p 6379:6379 -d redis_loc
```