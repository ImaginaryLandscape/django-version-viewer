import pip
from operator import itemgetter


def list_package_versions():
    installed_packages = pip.get_installed_distributions()
    results = [{"package_name": i.key, "package_version": i.version} for i in installed_packages]
    return sorted(results, key=itemgetter('package_name'))
