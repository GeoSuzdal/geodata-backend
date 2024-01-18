postgres:
	docker run -d \
	-p 5432:5432 \
	--env-file ./.env \
	--mount type=bind,source="%cd%\postgres_files",target=/data \
	postgres:latest
