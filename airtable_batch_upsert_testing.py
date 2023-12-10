from parsons.airtable.airtable import Airtable
import dotenv

dotenv.load_dotenv("/Users/matthewkrausse/PycharmProjects/general/dev.env")

# Create an Airtable object
base_key = "appoHKHk5Qi4NEChq"
table_name = "Test Table"

at = Airtable(
    base_key=base_key,
    table_name=table_name,
)

records = at.get_records()

# Alter the records to test the update
for record in records:
    record["Name"] = "Matt"

# Update the records
response = at.batch_upsert_records(records, fields_to_merge_on=["id"])

print(response)
