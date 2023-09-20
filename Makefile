.PHONY = openapi.json

openapi.json:
	curl -H 'Accept: application/json' http://localhost:8080/api/schema/ > openapi.json
