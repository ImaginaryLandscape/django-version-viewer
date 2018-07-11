from operator import itemgetter
import pkg_resources


def list_package_versions():
    """
    Returns a dict of installed pip packages

    {'package_name': "django", 'package_version': "1.8.18"}
    """
    installed_packages = pkg_resources.WorkingSet()
    results = [{"package_name": i.key, "package_version": i.version} for i in installed_packages]
    return sorted(results, key=itemgetter('package_name'))


def get_pip_packages_csv(writer):
    """
    Takes a csv writer and writes installed pip packages to it.
    """
    installed_packages = pkg_resources.WorkingSet()
    for i in installed_packages:
        writer.writerow([i.key, i.version])
    return writer
