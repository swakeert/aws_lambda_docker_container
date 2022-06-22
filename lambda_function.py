import json

import pyarrow.parquet as pq
from pyarrow import Table


def lambda_handler(event, context):
    t = Table.from_pydict({k: [v] for k, v in event.items()})
    file_name = "/tmp/example.parquet"
    pq.write_table(t, file_name)

    return {"statusCode": 200, "body": json.dumps("Success!")}
