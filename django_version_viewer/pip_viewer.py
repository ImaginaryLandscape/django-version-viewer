from importlib import metadata


def list_package_versions():
    """
    Returns a dict of installed pip packages

    {'package_name': "django", 'package_version': "1.8.18"}
    """
    results = [
        {
            "package_name": dist.metadata.get("Name", "").lower(),
            "package_version": dist.version,
            "package_url": dist.metadata.get("Home-page", "")
        }
        for dist in metadata.distributions()
    ]
    return sorted(results, key=lambda row: row["package_name"])


def get_pip_packages_csv(writer):
    """
    Takes a csv writer and writes installed pip packages to it.
    """
    for dist in metadata.distributions():
        name = dist.metadata.get("Name", "").lower()
        writer.writerow([name, dist.version])
    return writer
