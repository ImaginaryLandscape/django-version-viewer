from operator import itemgetter
import pkg_resources


def get_pkg_url(d):
    try:
        metadata = d._get_metadata(d.PKG_INFO)
        home_page = [m for m in metadata if m.startswith('Home-page:')]
        url = home_page[0].split(':', 1)[1].strip() if home_page else ''
        return url
    except AttributeError:
        return ''


def list_package_versions():
    """
    Returns a dict of installed pip packages

    {'package_name': "django", 'package_version': "1.8.18"}
    """
    installed_packages = pkg_resources.WorkingSet()
    results = [{"package_name": i.key, "package_version": i.version,
                "package_url": get_pkg_url(i)} for i in installed_packages]
    return sorted(results, key=itemgetter('package_name'))


def get_pip_packages_csv(writer):
    """
    Takes a csv writer and writes installed pip packages to it.
    """
    installed_packages = pkg_resources.WorkingSet()
    for i in installed_packages:
        writer.writerow([i.key, i.version])
    return writer
