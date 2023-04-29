import os

def get_package_path(package_name):
    """
    This function finds the path to the specified Debian package file.
    It assumes that the package file is stored in the /srv/salt/ directory.
    """
    return os.path.join('/srv/salt', package_name + '.deb')
