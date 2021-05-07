# improviser-api-client
Auto generated api client

used: https://github.com/triaxtec/openapi-python-client to generate a client.

It uses a converted v2 => v3 json. Which can be reconstructed with:

```
curl -X GET "https://converter.swagger.io/api/convert?url=https%3A%2F%2Fapi.improviser.education%2Fswagger.json" \
-H "accept: application/json"
```

## Setup

Create a venv, activate it and run: `pip install -r requirements.txt`

Generated a client with:

```bash
openapi-python-client generate --path improviser.json
```
