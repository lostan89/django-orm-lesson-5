from django.db import migrations
import phonenumbers

def convert_to_pure_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owners_phonenumber='+70000000000'):
        if not flat.owners_phonenumber:
            continue
        parse_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(parse_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(flat.owner_pure_phone)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20260203_2016'),
    ]

    operations = [
    migrations.RunPython(convert_to_pure_phonenumbers)
    ]

