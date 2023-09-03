import sys

from django.core.exceptions import ObjectDoesNotExist


def add_or_update_django_sites(apps=None, sites=None, fqdn=None):
    Site = apps.get_model('sites', 'Site')
    Site.objects.filter(name='example.com').delete()
    for site_id, site_name, _ in sites:
        try:
            site_obj = Site.objects.get(pk=site_id)
        except ObjectDoesNotExist:
            Site.objects.create(
                pk=site_id,
                name=site_name,
                domain=f'{site_name}.{fqdn}')
        else:
            site_obj.name = site_name
            site_obj.domain = f'{site_name}.{fqdn}'
            site_obj.save()
    sys.stdout.write(f'Updated sites for {fqdn}.\n')
    sys.stdout.flush()
