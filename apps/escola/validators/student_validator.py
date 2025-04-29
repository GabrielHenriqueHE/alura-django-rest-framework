import re

from rest_framework import serializers
from validate_docbr import CPF


class StudentValidator:
    class ValidationPatterns:
        PHONE_NUMBER_PATTERN = "[0-9]{2} [0-9]{5}-[0-9]{4}"

    def validate(self, data):
        if not data["name"].isalpha():
            raise serializers.ValidationError(
                {"name": "Name must contain only letters."}
            )

        if not CPF().validate(data["cpf"]):
            raise serializers.ValidationError({"cpf": "Invalid CPF provided."})

        if not self.__validate_phone_number(data["phone_number"]):
            raise serializers.ValidationError(
                {"phone_number": "Invalid phone number provided."}
            )

        return data

    def __validate_phone_number(self, phone_number):
        return re.findall(self.ValidationPatterns.PHONE_NUMBER_PATTERN, phone_number)
