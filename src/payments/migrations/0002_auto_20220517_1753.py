from django.db import migrations


def start_items(apps, schema_editor):
    Item = apps.get_model('payments', 'Item')
    Item.objects.create(name="Ball", description="Just a ball", price=0.99)
    Item.objects.create(name="Table", description="Just a table", price=2.99)
    Item.objects.create(name="Chair", description="Just a chair", price=3.99)


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [migrations.RunPython(start_items)]
