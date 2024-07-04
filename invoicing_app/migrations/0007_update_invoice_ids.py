# migrations/0007_update_invoice_ids.py
from django.db import migrations
import uuid

def generate_uuids(apps, schema_editor):
    cursor = schema_editor.connection.cursor()
    cursor.execute('SELECT id, invoice_id FROM invoicing_app_invoice')
    rows = cursor.fetchall()
    for row in rows:
        invoice_id = row[1]
        if not invoice_id or len(invoice_id) != 36:
            new_uuid = str(uuid.uuid4())
            cursor.execute('UPDATE invoicing_app_invoice SET invoice_id = %s WHERE id = %s', [new_uuid, row[0]])

class Migration(migrations.Migration):

    dependencies = [
        ('invoicing_app', '0006_alter_invoice_invoice_id'),  # Replace with the actual initial migration file name
    ]

    operations = [
        migrations.RunPython(generate_uuids),
    ]