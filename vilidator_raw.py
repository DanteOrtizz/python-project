from cerberus import Validator

body = {
    "data": {
        "element_one": 123.98,
        "element_two": "olaMundo",
        "element_three": "789",
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "element_one": { "type": "float", "required": True, "empty": False },
            "element_two": { "type": "string", "required": True, "empty": True },
            "element_three": { "type": "string", "required": False, "empty": False },
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print('Body OK')
