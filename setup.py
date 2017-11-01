from setuptools import setup, find_packages

description_files = ["README.rst", "AUTHORS.rst", "CHANGELOG.rst"]

setup(
    name="django-feersum-nlu",
    description="A django feersum nlu wrapper with helper methods and reusable views.",
    long_description="".join([open(f, "r").read() for f in description_files]),
    version="0.0.1",
    author="Praekelt Consulting",
    author_email="dev@praekelt.com",
    license="BSD",
    url="http://github.com/praekelt/django-feersum-nlu",
    packages=find_packages(),
    dependency_links=[],
    install_requires=[
        "django"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
    include_package_data=True
)
