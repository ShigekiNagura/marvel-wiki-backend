# ローカル開発用のシェル
# DBサーバのみコンテナ

source ./.venv/bin/activate

docker-compose down
docker-compose up -d

cd ./src

python manage.py runserver