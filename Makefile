.PHONY = openapi.json

openapi.json:
	curl http://localhost:8080/api/docs/?format=openapi > openapi.json
