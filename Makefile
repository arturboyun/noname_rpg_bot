PYTHONPATH := $(shell pwd):${PYTHONPATH}

dev:
	python -m bot start

docker-up-db:
	docker-compose up postgres redis -d

docker-up:
	docker0-compose up -d
