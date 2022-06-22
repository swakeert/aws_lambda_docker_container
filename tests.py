import pyarrow.parquet as pq

from .lambda_function import lambda_handler


def test_lambda_handler():
    event = {"key": "value"}
    context = {}
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    d = pq.read_table("/tmp/example.parquet").to_pydict()
    assert d["key"] == ["value"]
