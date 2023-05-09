movies_validator = {
    "$jsonSchema": {
        "bsonType":"object",
        "required": ["name", "rating", "length", "categories", "stars"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and it is required"
            },
            "rating": {
                "bsonType": "double",
                "description": "must be a double and it is required"
            },
            "year": {
                "bsonType": "int",
                "description": "must be an int and it is NOT required"
            },
            "length": {
                "bsonType": "string",
                "description": "must be a string and it is required"
            },
            "categories": {
                "bsonType": "array",
                "items": {
                    "bsonType": "string",
                    "description": "must be a string and it is required"
                },
                "description": "must be a string and it is required"
            },
            "description": {
                "bsonType": "string",
                "description": "must be a string and it is NOT required"
            },
            "director": {
                "bsonType": "string",
                "description": "must be a string and it is NOT required"
            },
            "stars": {
                "bsonType": "array",
                "items": {
                    "bsonType": "string",
                    "description": "must be a string and it is required"
                },
                "description": "must be a string and it is required"
            },
            "writers": {
                "bsonType": "array",
                "items": {
                    "bsonType": "string",
                    "description": "must be a string and it is NOT required"
                },
                "description": "must be a string and it is NOT required"
            }
        }
    }
}