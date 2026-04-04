import pytest
from python.core.validation_utils import validate_id, validate_required_fields


def test_validate_id_valid():
    result = validate_id(10, "client_id")
    assert result is None


def test_validate_id_invalid_type():
    result = validate_id("abc", "client_id")
    assert result["status"] == "failed"
    assert "integer" in result["error"]


def test_validate_id_negative():
    result = validate_id(-5, "client_id")
    assert result["status"] == "failed"
    assert "greater than 0" in result["error"]


def test_validate_required_fields_valid():
    data = {"name": "John", "age": 25}
    result = validate_required_fields(data, ["name", "age"])
    assert result is None


def test_validate_required_fields_missing():
    data = {"name": "John"}
    result = validate_required_fields(data, ["name", "age"])
    assert result["status"] == "failed"
    assert "Missing required fields" in result["error"]