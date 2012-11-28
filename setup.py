# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re

# Dynamically calculate the version based on filizver.VERSION.
VERSION = (0, 1, 0, 'beta', 0)

def get_version(version=None):
    """Derives a PEP386-compliant version number from VERSION."""
    if version is None:
        version = VERSION
    assert len(version) == 5
    assert version[3] in ('alpha', 'beta', 'rc', 'final')

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|c}N - for alpha, beta and rc releases

    parts = 2 if version[2] == 0 else 3
    main = '.'.join(str(x) for x in version[:parts])

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        # At the toplevel, this would cause an import loop.
        from django.utils.version import get_svn_revision
        svn_revision = get_svn_revision()[4:]
        if svn_revision != 'unknown':
            sub = '.dev%s' % svn_revision

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'c'}
        sub = mapping[version[3]] + str(version[4])

    return main + sub

setup(
    name="django-cmskit",
    version=get_version(),
    description = "A collection of useful Django CMS extensions.",
    long_description=open("README").read(),
    author = "Ozgur Gunes",
    author_email = "o.gunes@gmail.com",
    url = "http://github.com/ozgurgunes/django-cmskit/",
    packages=find_packages(),
    install_requires=[
        'django>=1.4',
        'django-cms==2.3.1',
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    zip_safe=False,
)
