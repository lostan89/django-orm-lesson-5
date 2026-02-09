from django.db import migrations
import phonenumbers

def convert_to_pure_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(owners_phonenumber='+70000000000'):
        if not flat.owners_phonenumber:
            continue      
        parse_phone = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parse_phone):
            flat.owner_pure_phone = phonenumbers.format_number(parse_phone, phonenumbers.PhoneNumberFormat.E164)
        print(flat.owner_pure_phone)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20260205_2134'),
    ]

    operations = [
    migrations.RunPython(convert_to_pure_phonenumbers)
    ]


