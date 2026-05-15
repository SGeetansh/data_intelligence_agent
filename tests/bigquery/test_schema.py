import sys
from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parents[2]))
from data_intelligence_agent.tools.bigquery.schema import get_schema

schema = get_schema(
    "bigquery-public-data.thelook_ecommerce"
)

print(schema)