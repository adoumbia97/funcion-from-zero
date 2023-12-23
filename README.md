# funcion-from-zero
[![Python Application test with github actions](https://github.com/adoumbia97/funcion-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/adoumbia97/funcion-from-zero/actions/workflows/main.yml)


### To call a microservice

Something like this:
```bash
curl -X 'POST' \
  'https://effective-engine-qp954vwvrp6f9jg7-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Facebook"
}'

```